from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from .credsApi import add_account, retrieve_accounts
import email
import base64
from collections import Counter
from sklearn.svm import LinearSVC
import dateutil.parser
import multiprocessing as mp
from .gmail import *

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

def remove_common_words(dict):
        words = list(dict.keys())
        for word in words:
            if word in commonWordList:
                del (dict[word])
            elif len(word) <= 2:
                del (dict[word])
            elif len(word) > 30:
                del (dict[word])
            # elif not word.isalpha():
            #     del (dict[word])

def mcw_from_label(label, app_token):
    email_list = get_email_details_from_label(label, app_token)
    word_list = []
    for email in email_list:
        email_body = email["body"]
        body_list = email_body.split()
        word_list += body_list
    mcw = Counter(word_list)
    remove_common_words(mcw)
    mcw = mcw.most_common(200)
    return mcw

