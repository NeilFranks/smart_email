from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from .credsApi import add_account, retrieve_accounts
import email
import base64
from collections import Counter
from sklearn.linear_model import SGDClassifier
import numpy as np
import dateutil.parser
import multiprocessing as mp
import random
from .gmail import *

commonWordList = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "her",
    "hers",
    "herself",
    "it",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "can",
    "will",
    "just",
    "don",
    "should",
    "now",
    "nbsp",
    "enron",
    "=C2=A0",
    "=0A",
    "=0A=0A=C2=A0",
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "2019",
]

MCW_SIZE = 500


def remove_common_words(dict):
    words = list(dict.keys())
    for word in words:
        lower_word = word.lower()
        if lower_word in commonWordList:
            del dict[word]
        elif len(lower_word) <= 2:
            del dict[word]
        elif len(lower_word) > 30:
            del dict[word]
        # elif not word.isalpha():
        #     del (dict[word])


# This naming is going to have to change.
def mcw_from_label(label, app_token):
    n = 100
    email_list = get_email_details_from_label(n, label, app_token)
    second_list = get_emails_details_not_from_label(
        label, None, app_token, len(email_list)
    )

    full_list = second_list + email_list
    word_list = []
    for email in full_list:
        email_body = email["body"]
        email_body = (
            email_body.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        email_subj = email["subject"]
        email_subj = (
            email_subj.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        subj_list = email_subj.split()
        body_list = email_body.split()
        word_list += body_list
        word_list += subj_list
    mcw = Counter(word_list)
    remove_common_words(mcw)
    mcw = mcw.most_common(MCW_SIZE)
    train_labels = np.zeros(len(full_list))
    train_labels[len(email_list) :] = 1

    train_matrix = extract_features(mcw, full_list)

    classifier = SGDClassifier(loss="modified_huber", max_iter=100, warm_start=True)
    # Here's the model
    classifier.partial_fit(train_matrix, train_labels)
    mail = get_email_details_from_label("Not_Vice", app_token)
    test_matrix = extract_features(mcw, mail)
    prediction = classifier.predict(test_matrix)
    # print(prediction)
    return mcw

    # This naming is going to have to change.


def classifier_from_label(label, notEmails, app_token):
    n = 30
    email_list = get_email_details_from_label(n, label, app_token)
    n = len(email_list)  # actual emails gotten might have been less than requested

    # if you were not provided enough "not in category" emails, go get some random ones from some other labels.
    if not notEmails or len(notEmails) < n:
        second_list = get_emails_details_not_from_label(label, notEmails, app_token, n)
    else:
        second_list = notEmails[0:n]

    full_list = second_list + email_list
    word_list = []
    for email in full_list:
        email_body = email["body"]
        email_body = (
            email_body.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        email_subj = email["subject"]
        email_subj = (
            email_subj.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        subj_list = email_subj.split()
        body_list = email_body.split()
        word_list += body_list
        word_list += subj_list
    mcw = Counter(word_list)
    remove_common_words(mcw)
    mcw = mcw.most_common(MCW_SIZE)
    train_labels = np.zeros(len(full_list))
    train_labels[n:] = 1

    train_matrix = extract_features(mcw, full_list)

    # create and return classifier
    classifier = SGDClassifier(loss="modified_huber", max_iter=100, warm_start=True)
    classifier.fit(train_matrix, train_labels)

    return classifier, mcw


def classifier_from_emails_and_notEmails(label, email_list, notEmails, app_token):
    n = len(email_list)

    # if you were not provided enough "not in category" emails, go get some random ones from some other labels.
    if not notEmails or len(notEmails) < n:
        second_list = get_emails_details_not_from_label(label, notEmails, app_token, n)
    else:
        second_list = notEmails[0:n]

    print("\ngood\n")
    for email in email_list:
        print(email["subject"])

    print("\nbad\n")
    for email in second_list:
        print(email["subject"])

    full_list = second_list + email_list

    word_list = []
    for email in full_list:
        email_body = email["body"]
        email_body = (
            email_body.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        email_subj = email["subject"]
        email_subj = (
            email_subj.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        subj_list = email_subj.split()
        body_list = email_body.split()
        word_list += body_list
        word_list += subj_list
    mcw = Counter(word_list)
    remove_common_words(mcw)
    mcw = mcw.most_common(MCW_SIZE)
    train_labels = np.zeros(len(full_list))
    train_labels[n:] = 1

    train_matrix = extract_features(mcw, full_list)

    # create and return classifier
    classifier = SGDClassifier()
    print("ah")
    classifier.partial_fit(train_matrix, train_labels)
    print(":(")

    return classifier, mcw


def update_classifier_from_emails_and_notEmails(
    classifier, label, email_list, notEmails, app_token
):
    n = len(email_list)
    print("agag")
    print(n)
    print("aohoh")

    # if you were not provided enough "not in category" emails, go get some random ones from some other labels.
    if not notEmails or len(notEmails) < n:
        second_list = get_emails_details_not_from_label(label, notEmails, app_token, n)
    else:
        second_list = notEmails[0:n]

    print("\ngood\n")
    for email in email_list:
        print(email["subject"])

    print("\nbad\n")
    for email in second_list:
        print(email["subject"])

    full_list = second_list + email_list

    word_list = []
    for email in full_list:
        email_body = email["body"]
        email_body = (
            email_body.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        email_subj = email["subject"]
        email_subj = (
            email_subj.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        subj_list = email_subj.split()
        body_list = email_body.split()
        word_list += body_list
        word_list += subj_list
    mcw = Counter(word_list)
    remove_common_words(mcw)
    mcw = mcw.most_common(MCW_SIZE)
    train_labels = np.zeros(len(full_list))
    train_labels[n:] = 1

    train_matrix = extract_features(mcw, full_list)

    # update and return classifier
    print(len(train_matrix))
    shuffledRange = list(range(len(train_matrix)))
    n_iter = 1000
    for n in range(n_iter):
        random.shuffle(shuffledRange)
        shuffledX = [train_matrix[i] for i in shuffledRange]
        shuffledY = [train_labels[i] for i in shuffledRange]
        classifier.partial_fit(shuffledX, shuffledY)

    return classifier, mcw


def extract_features(mcw, emails):
    features_matrix = np.zeros((len(emails), MCW_SIZE))
    emailID = 0
    for email in emails:
        body = email["body"]
        body = (
            body.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        body_list = body.split()
        for word in body_list:
            for i in range(len(mcw)):
                if word == mcw[i][0]:
                    # print(word, mcw[i][0], i)
                    features_matrix[emailID, i] += 1
                    break
        sub = email["subject"]
        sub = (
            sub.replace("=0A", " ")
            .replace("=C2", " ")
            .replace("=A0", " ")
            .replace("=3F", "?")
        )
        sub_list = sub.split()
        for word in sub_list:
            if word in mcw:
                wordID = mcw.index(word)
                features_matrix[emailID, wordID] += 1
        # print(features_matrix[emailID])
        emailID = emailID + 1
    return features_matrix
