import requests
import datetime
import imaplib
import email
import re
from django.core import serializers
from sklearn.svm import LinearSVC
from collections import Counter

class Category(object):

    def __init__(self, categoryName, time, model):
        self.categoryName = categoryName
        self.time = time
        self.model = model

def read_email(raw_email):
    mail = email.message_from_bytes(raw_email)
    mail_dict = { "Sender":"*sender*", "Date":"*date*", "Subject":"*subject*", "Body":"*body*" }
    headers = mail._headers
    for h in headers:
        if h[0] == "From":
            mail_dict["Sender"] = h[1]
        elif h[0] == "Subject":
            mail_dict["Subject"] = h[1]
        elif h[0] == "Date":
            mail_dict["Date"] = h[1]

    for part in mail.walk():
        if part.get_content_type() == "text/plain":  # ignore attachments/html
            body = part.get_payload(decode=True)

            try:
                body = body.decode()
            except:
                # figure out which charset this is using
                try:
                    payload = mail._payload
                    for element in payload:
                        subheaders = element._headers
                        for h in subheaders:
                            if h[0] == 'Content-Type' or h[0] == 'Content-type':
                                charset = h[1].split()[1].split("=")[1]
                except:
                    subheaders = mail._headers
                    for h in subheaders:
                        if h[0] == 'Content-Type' or h[0] == 'Content-type':
                            charset = h[1].split()[1].split("=")[1]

                # now you have the charset, but sometimes it has quotation marks or a semicolon. remove any
                charset = charset.replace("\"", "")
                charset = charset.replace(";", "")

                #make it lowercase
                charset = charset.lower()

                #decode body according to charset
                mail_dict["Body"] = body.decode(charset)
    
    return mail_dict

def remove_common_words(word_frequency):
    commonWordList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                      "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom",
                      "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
                      "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but",
                      "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
                      "against", "between", "into", "through", "during", "before", "after", "above", "below", "to",
                      "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then",
                      "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few",
                      "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                      "too", "very", "can", "will", "just", "don", "should", "now", "nbsp", "enron" ]

    words = list(word_frequency.keys())
    for word in words:
        if word in commonWordList:
            del (word_frequency[word])
        elif len(word) <= 2:
            del (word_frequency[word])

    return word_frequency

def get_mcw_from_emails(list_of_emails):
    list_of_body_words = []
    for mail in list_of_emails:
        body = mail["Body"].split()
        if body:
            list_of_body_words += body
    
    word_freq = Counter(list_of_body_words)
    word_freq = remove_common_words(word_freq)
    return word_freq.most_common(3000)

def check_email(con, msg, category):
    con.select(mailbox='"{}"'.format(category.categoryName))
    email_list = list()
    _, data = con.search(None, ("(ALL)"))
    for mail in data[0].split():
        _, raw_data = con.fetch(mail, '(RFC822)')
        new_msg = read_email(raw_data[0][1])
        email_list.append(new_msg)
    # END OFF POINT
    # TODO: get mcw from all emails
    # Have train_labels [0:len(category_emails)] be 0 | [len(category_emails):len(all_excluding_category_emails)] be 1
    # extract features into training matrix
    # train linearSVC()
    # Decide if proper in category
    mcw = get_mcw_from_emails(email_list)
    train_labels = np.zeros()
    return True

def scan_emails(categories):
    con = imaplib.IMAP4_SSL('imap.gmail.com')
    con.login('capstonespamtest@gmail.com', 'BigMike1')
    con.select(mailbox='"various almost-spam"')
    _, data = con.search(None, "(ALL)")
    for mail in data[0].split():
        _, new_data = con.fetch(mail, '(RFC822)')
        _, msgID = con.fetch(mail, '(X-GM-MSGID)')
        msgID = re.findall(r"X-GM-MSGID (\d+)", str(msgID))[0]
        msg = read_email(new_data[0][1])
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        for category in categories:
            if category.time < local_date:
                valid_email = check_email(con, msg, category)
                if (valid_email):
                    uid = con.search(None, '(X-GM-MSGID) "%s"' % msgID)
                    uid = uid[1][0]
                    con.uid('COPY', uid, '"{}"'.format(category.categoryName))


#a = Category("Sports", datetime.datetime.now())
#
# 1.
# for each email:
#   for each category:
#      if curr_category.model_time < unseen_email.time:
#         run model on that email
#         if that email belongs in category:
#            add email to that category
#         go on to next category
#
#            


