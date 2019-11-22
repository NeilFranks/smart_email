from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from .credsApi import add_account, retrieve_accounts
import email
import base64
import quopri
import re
import dateutil.parser
import multiprocessing as mp
import googleapiclient

# If modifying these scopes, delete the stored token.
SCOPES = ["https://mail.google.com/"]


def connect_new_account(app_token):
    print("trying to do the thing")
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)

    print("creds: %s" % creds)
    # get what you need from the profile through GMail API
    service = build("gmail", "v1", credentials=creds)
    profile = service.users().getProfile(userId="me").execute()
    address = profile.get("emailAddress")

    print("built the service")

    # call api to add creds to the associated user
    content = add_account(creds, address, app_token)

    print("added account")

    return content


def get_single_email(address, email_id, app_token):
    """
    Returns the body text of the given email send to the given address
    """
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if address == connection.get("address"):
            # get access to emails
            creds = connection.get("creds")
            service = build("gmail", "v1", credentials=creds)
            results = (
                service.users()
                .messages()
                .get(userId="me", id=email_id, format="raw")
                .execute()
            )

            msg_str = base64.urlsafe_b64decode(results["raw"].encode("ASCII"))
            mime_msg = email.message_from_bytes(msg_str)
            messageMainType = mime_msg.get_content_maintype()
            if "multipart" in messageMainType:
                return get_email_body(mime_msg, messageMainType)
            elif messageMainType == "text/plain":
                return mime_msg.get_payload()
    return None


def get_email_body(msg, message_type):
    output = ""
    if "multipart" in message_type:
        for part in msg.get_payload():
            m_type = part["Content-Type"].split()[0].replace(";", "")
            if "multipart" in m_type:
                output = get_email_body(part, m_type)
            elif "text" in m_type and "html" not in m_type:
                try:
                    encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
                    charset, encoding, encoded_text = re.match(
                        encoded_word_regex, part.get_payload()
                    ).groups()
                    if encoding is "B":
                        body = base64.b64decode(encoded_text)
                    elif encoding is "Q":
                        body = quopri.decodestring(encoded_text)
                    output = body.decode()
                    # output = base64.urlsafe_b64decode(part.get_payload()).decode(encoding)
                except:
                    output = part.get_payload()
                break
    elif "text" in m_type and "html" not in m_type:
        try:
            encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
            charset, encoding, encoded_text = re.match(
                encoded_word_regex, part.get_payload()
            ).groups()
            if encoding is "B":
                body = base64.b64decode(encoded_text)
            elif encoding is "Q":
                body = quopri.decodestring(encoded_text)
            output = body.decode()
            # output = base64.urlsafe_b64decode(part.get_payload()).decode(encoding)
        except:
            output = part.get_payload()
    return output


def get_email_details(n, before_time, label_id, app_token):
    """
    Returns id, date (and time), from, and subject of the most recent n emails sent to the address.
    """

    connections = retrieve_accounts(app_token)
    detailsList = []

    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.map` the `get_email_details_from_account()`
    detailsList = pool.map(
        get_email_details_from_account,
        [(connection, n, before_time, label_id) for connection in connections],
    )  # Returns a list of lists

    # Flatten the list of lists
    detailsList = [ent for sublist in detailsList for ent in sublist]

    # Step 3: Don't forget to close
    pool.close()

    if detailsList:
        detailsList.sort(
            key=lambda x: dateutil.parser.parse(x.get("date")), reverse=True
        )
        detailsList = detailsList[0 : int(n)]

    return detailsList


def get_email_details_from_label(label, app_token):
    """
    Returns id, date (and time), from, and subject of the most recent n emails sent to the address.
    """

    connections = retrieve_accounts(app_token)
    detailsList = []

    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.map` the `get_email_details_from_account()`
    detailsList = pool.map(
        get_emails_from_label, [(connection, label) for connection in connections]
    )  # Returns a list of lists

    # Flatten the list of lists
    detailsList = [ent for sublist in detailsList for ent in sublist]

    # Step 3: Don't forget to close
    pool.close()

    return detailsList


def get_emails_details_not_from_label(label, app_token, size):
    """
    Returns id, date (and time), from, and subject of the most recent n emails sent to the address.
    """

    connections = retrieve_accounts(app_token)
    detailsList = []

    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.map` the `get_email_details_from_account()`
    detailsList = pool.map(
        get_emails_not_from_label,
        [(connection, label, size) for connection in connections],
    )  # Returns a list of lists

    # Flatten the list of lists
    detailsList = [ent for sublist in detailsList for ent in sublist]

    # Step 3: Don't forget to close
    pool.close()

    return detailsList


def get_connected_addresses(app_token):
    """
    Returns list of email addresses associated with the user
    """
    connections = retrieve_accounts(app_token)

    addressList = []
    for connection in connections:
        address = connection.get("address")
        if address and "@" in address:  # TODO: better input validation
            addressList.append(address)

    return addressList


def get_emails_not_from_label(connectionAndLabel):
    detailsList = []

    connection = connectionAndLabel[0]
    label = connectionAndLabel[1]
    size = connectionAndLabel[2]

    # get access to emails
    creds = connection.get("creds")
    service = build("gmail", "v1", credentials=creds)
    response = service.users().labels().list(userId="me").execute()
    labels = response["labels"]

    label_id = list()
    for i in labels:
        if i["name"] == label:
            label_id.append(i["id"].lstrip())
            break

    results = (
        service.users()
        .messages()
        .list(userId="me", maxResults=size, q="is:read -label:{}".format(label))
        .execute()
    )
    msgs = results.get("messages", [])

    if not msgs:
        print("No messages")
    else:
        for msg in msgs:

            message = (
                service.users()
                .messages()
                .get(userId="me", id=msg["id"], format="raw")
                .execute()
            )

            msg_str = base64.urlsafe_b64decode(message["raw"].encode("ASCII"))
            mime_msg = email.message_from_bytes(msg_str)
            subject = ""
            body = ""
            try:
                encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
                charset, encoding, encoded_text = re.match(
                    encoded_word_regex, mime_msg["Subject"]
                ).groups()
                if encoding is "B":
                    subject = base64.b64decode(encoded_text)
                elif encoding is "Q":
                    subject = quopri.decodestring(encoded_text)
                subject = subject.decode()
            except:
                subject = mime_msg["Subject"]
            messageMainType = mime_msg.get_content_maintype()
            if "multipart" in messageMainType:
                body = get_email_body(mime_msg, messageMainType)
            elif messageMainType == "text/plain":
                body = mime_msg.get_payload()
            # isolate the details
            myId = message.get("id")
            detailsList.append(
                {
                    "address": connection.get("address"),
                    "id": myId,
                    "body": body,
                    "subject": subject,
                }
            )

    return detailsList


def get_emails_from_label(connectionAndLabel):
    detailsList = []

    connection = connectionAndLabel[0]
    label = connectionAndLabel[1]

    # get access to emails
    creds = connection.get("creds")
    service = build("gmail", "v1", credentials=creds)
    response = service.users().labels().list(userId="me").execute()
    labels = response["labels"]

    label_id = list()
    for i in labels:
        if i["name"] == label:
            label_id.append(i["id"].lstrip())
            break

    results = service.users().messages().list(userId="me", labelIds=label_id).execute()
    msgs = results.get("messages", [])

    if not msgs:
        print("No messages")
    else:
        for msg in msgs:
            message = (
                service.users()
                .messages()
                .get(userId="me", id=msg["id"], format="raw")
                .execute()
            )
            # payload = message.get('payload')
            # headers = payload.get('headers')
            # subject = ""
            # for header in headers:
            #     name = header.get('name')
            #     if name == 'Subject':
            #         subject = header.get('value')

            msg_str = base64.urlsafe_b64decode(message["raw"].encode("ASCII"))
            mime_msg = email.message_from_bytes(msg_str)
            subject = ""
            body = ""
            try:
                encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
                charset, encoding, encoded_text = re.match(
                    encoded_word_regex, mime_msg["Subject"]
                ).groups()
                if encoding is "B":
                    subject = base64.b64decode(encoded_text)
                elif encoding is "Q":
                    subject = quopri.decodestring(encoded_text)
                subject = subject.decode()
            except:
                subject = mime_msg["Subject"]
            messageMainType = mime_msg.get_content_maintype()
            if "multipart" in messageMainType:
                body = get_email_body(mime_msg, messageMainType)
            elif messageMainType == "text/plain":
                body = mime_msg.get_payload()
            # isolate the details
            myId = message.get("id")
            detailsList.append(
                {
                    "address": connection.get("address"),
                    "id": myId,
                    "body": body,
                    "subject": subject,
                }
            )

    return detailsList


def get_email_details_from_account(connectionAndN):

    detailsList = []

    connection = connectionAndN[0]
    n = connectionAndN[1]
    before_time = connectionAndN[2]
    label_dict = connectionAndN[
        3
    ]  # label_dict is a dictionary; keys are email addresses, values are associated label_ids

    # get access to emails
    creds = connection.get("creds")
    service = build("gmail", "v1", credentials=creds)
    if label_dict:
        address = connection.get("address")
        list_of_labels = label_dict[address]
        results = (
            service.users()
            .messages()
            .list(
                userId="me",
                labelIds=list_of_labels,
                maxResults=n,
                q="before:{}".format(before_time),
            )
            .execute()
        )
    else:
        results = (
            service.users()
            .messages()
            .list(userId="me", maxResults=n, q="before:{}".format(before_time))
            .execute()
        )
    labels = results.get("messages", [])

    if not labels:
        print("No labels found.")
    else:
        for label in labels:
            message = (
                service.users()
                .messages()
                .get(
                    userId="me",
                    id=label["id"],
                    format="metadata",
                    metadataHeaders=["Date", "From", "Subject"],
                )
                .execute()
            )

            # isolate the details
            myId = message.get("id")
            labels = message.get("labelIds")
            payload = message.get("payload")
            # print(payload)
            headers = payload.get("headers")

            for header in headers:
                name = header.get("name")
                if name == "Date":
                    date = header.get("value")
                if name == "From":
                    sender = header.get("value")
                if name == "Subject":
                    subject = header.get("value")

            # sender looks like "name <address@gmail.com>". We just want the first part
            sender = sender.split("<")[0]

            snippet = message.get("snippet")

            detailsList.append(
                {
                    "address": connection.get("address"),
                    "id": myId,
                    "date": date,
                    "unread": "UNREAD" in labels,
                    "labels": labels,
                    "sender": sender,
                    "snippet": snippet,
                    "subject": subject,
                }
            )

    return detailsList


def create_label(label_object, app_token):
    labelDict = (
        dict()
    )  # for associating an email address with the label ID this new label corresponds to

    connections = retrieve_accounts(app_token)
    for connection in connections:
        creds = connection.get("creds")
        service = build("gmail", "v1", credentials=creds)
        try:
            label = (
                service.users()
                .labels()
                .create(userId="me", body=label_object)
                .execute()
            )
            address = connection.get("address")
            labelDict[address] = [label["id"]]
        except googleapiclient.errors.HttpError as e:
            print(e)
            return e.resp
    return labelDict


def batch_unmark_from_something(account, list_of_ids, list_of_labels, app_token):
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if account == connection.get("address"):
            creds = connection.get("creds")
            service = build("gmail", "v1", credentials=creds)
            messages = (
                service.users()
                .messages()
                .batchModify(
                    userId="me",
                    body={"ids": list_of_ids, "removeLabelIds": list_of_labels},
                )
                .execute()
            )


def batch_mark_as_something(addressDict, label_dict, app_token):
    for address in addressDict:
        list_of_ids = addressDict[address]
        connections = retrieve_accounts(app_token)
        for connection in connections:
            if address == connection.get("address"):
                list_of_labels = label_dict[address]
                creds = connection.get("creds")
                service = build("gmail", "v1", credentials=creds)
                messages = (
                    service.users()
                    .messages()
                    .batchModify(
                        userId="me",
                        body={"ids": list_of_ids, "addLabelIds": list_of_labels},
                    )
                    .execute()
                )


def single_mark_as_read(account, message_id, app_token):
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if account == connection.get("address"):
            creds = connection.get("creds")
            service = build("gmail", "v1", credentials=creds)
            message = (
                service.users()
                .messages()
                .modify(userId="me", id=message_id, body={"removeLabelIds": ["UNREAD"]})
                .execute()
            )


def single_mark_as_unread(account, message_id, app_token):
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if account == connection.get("address"):
            creds = connection.get("creds")
            service = build("gmail", "v1", credentials=creds)
            message = (
                service.users()
                .messages()
                .modify(userId="me", id=message_id, body={"addLabelIds": ["UNREAD"]})
                .execute()
            )


def batch_mark_as_read(account, list_of_ids, app_token):
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if account == connection.get("address"):
            creds = connection.get("creds")
            service = build("gmail", "v1", credentials=creds)
            messages = (
                service.users()
                .messages()
                .batchModify(
                    userId="me", body={"ids": list_of_ids, "removeLabelIds": ["UNREAD"]}
                )
                .execute()
            )


def batch_mark_as_unread(account, list_of_ids, app_token):
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if account == connection.get("address"):
            creds = connection.get("creds")
            service = build("gmail", "v1", credentials=creds)
            messages = (
                service.users()
                .messages()
                .batchModify(
                    userId="me", body={"ids": list_of_ids, "addLabelIds": ["UNREAD"]}
                )
                .execute()
            )


def trash_message(account, message_id, app_token):
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if account == connection.get("address"):
            creds = connection.get("creds")
            service = build("gmail", "v1", credentials=creds)
            service.users().messages().trash(userId=account, id=message_id).execute()


if __name__ == "__main__":
    tok = "5333867a0eeb9d3f7c29eb404ced841e663ba0816aeeffbe10d3c6e3396d2538"
    bil = get_email_details("neilcapstonetest@gmail.com", 2, tok)
    hum = get_single_email("neilcapstonetest@gmail.com", "16e1ffd1248982ac", tok)

