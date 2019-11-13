from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from .credsApi import add_account, retrieve_accounts
import email
import base64
import dateutil.parser
import multiprocessing as mp

# If modifying these scopes, delete the stored token.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def connect_new_account(app_token):
    print("trying to do the thing")
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    print("creds: %s" % creds)
    # get what you need from the profile through GMail API
    service = build('gmail', 'v1', credentials=creds)
    profile = service.users().getProfile(userId='me').execute()
    address = profile.get('emailAddress')

    print("built the service")

    # call api to add creds to the associated user
    content = add_account(creds, address, app_token)

    print("added account")

    return content


def get_single_email(address, email_id, app_token):
    '''
    Returns the body text of the given email send to the given address
    '''
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if address == connection.get("address"):
            # get access to emails
            creds = connection.get("creds")
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().get(
                userId='me', id=email_id, format='raw').execute()

            msg_str = base64.urlsafe_b64decode(results['raw'].encode('ASCII'))
            mime_msg = email.message_from_bytes(msg_str)
            messageMainType = mime_msg.get_content_maintype()
            if 'multipart' in messageMainType:
                return get_email_body(mime_msg, messageMainType)
            elif messageMainType == 'text/plain':
                return mime_msg.get_payload()
    return None


def get_email_body(msg, message_type):
    if 'multipart' in message_type:
        for part in msg.get_payload():
            m_type = part["Content-Type"].split()[0].replace(";", "")
            if 'multipart' in m_type:
                output = get_email_body(part, m_type)
            elif 'text' in m_type:
                encoding = part["Content-Type"].split()[1].split("=")[1].lower()
                try:
                    output = base64.urlsafe_b64decode(part.get_payload()).decode(encoding)
                except:
                    output = part.get_payload()
                break
    elif 'text' in m_type:
        encoding = part["Content-Type"].split()[1].split("=")[1].lower()
        try:
            output = base64.urlsafe_b64decode(part.get_payload()).decode(encoding)
        except:
            output = part.get_payload()
    return output


def get_email_details(n, app_token):
    '''
    Returns id, date (and time), from, and subject of the most recent n emails sent to the address.
    '''

    connections = retrieve_accounts(app_token)
    detailsList = []

    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.map` the `get_email_details_from_account()`
    detailsList = pool.map(get_email_details_from_account, [(
        connection, n) for connection in connections])  # Returns a list of lists

    # Flatten the list of lists
    detailsList = [ent for sublist in detailsList for ent in sublist]

    # Step 3: Don't forget to close
    pool.close()

    if detailsList:
        detailsList.sort(key=lambda x: dateutil.parser.parse(
            x.get("date")), reverse=True)
        detailsList = detailsList[0:int(n)]

    return detailsList


def get_email_details_from_label(label, app_token):
    '''
    Returns id, date (and time), from, and subject of the most recent n emails sent to the address.
    '''

    connections = retrieve_accounts(app_token)
    detailsList = []

    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.map` the `get_email_details_from_account()`
    detailsList = pool.map(get_emails_from_label, [(
        connection, label) for connection in connections])  # Returns a list of lists

    # Flatten the list of lists
    detailsList = [ent for sublist in detailsList for ent in sublist]

    # Step 3: Don't forget to close
    pool.close()

    return detailsList


def get_connected_addresses(app_token):
    '''
    Returns list of email addresses associated with the user
    '''
    connections = retrieve_accounts(app_token)

    addressList = []
    for connection in connections:
        address = connection.get("address")
        if address and "@" in address:  # TODO: better input validation
            addressList.append(address)

    return addressList


def get_emails_from_label(connectionAndLabel):
    detailsList = []

    connection = connectionAndLabel[0]
    label = connectionAndLabel[1]

    # get access to emails
    creds = connection.get("creds")
    service = build('gmail', 'v1', credentials=creds)
    response = service.users().labels().list(userId='me').execute()
    labels = response['labels']

    label_id = list()
    for i in labels:
        if i["name"] == label:
            label_id.append(i["id"].lstrip())
            break

    results = service.users().messages().list(userId='me', labelIds=label_id).execute()
    msgs = results.get('messages', [])

    if not msgs:
        print("No messages")
    else:
        for msg in msgs:

            message = service.users().messages().get(
                userId='me', id=msg["id"], format='raw').execute()

            msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
            mime_msg = email.message_from_bytes(msg_str)
            messageMainType = mime_msg.get_content_maintype()
            if 'multipart' in messageMainType:
                body = get_email_body(mime_msg, messageMainType)
            elif messageMainType == 'text/plain':
                body = mime_msg.get_payload()
            print(body)
            # isolate the details
            myId = message.get('id')
            detailsList.append(
                {
                    'address': connection.get("address"),
                    'id': myId,
                    'body': body
                })

    return detailsList


def get_email_details_from_account(connectionAndN):

    detailsList = []

    connection = connectionAndN[0]
    n = connectionAndN[1]

    # get access to emails
    creds = connection.get("creds")
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', maxResults=n).execute()
    labels = results.get('messages', [])

    if not labels:
        print('No labels found.')
    else:
        for label in labels:
            message = service.users().messages().get(
                userId='me', id=label['id'], format='metadata',
                metadataHeaders=['Date', 'From', 'Subject']).execute()

            # isolate the details
            myId = message.get('id')
            labels = message.get('labelIds')
            payload = message.get('payload')
            #print(payload)
            headers = payload.get('headers')

            for header in headers:
                name = header.get('name')
                if name == 'Date':
                    date = header.get('value')
                if name == 'From':
                    sender = header.get('value')
                if name == 'Subject':
                    subject = header.get('value')

            # sender looks like "name <address@gmail.com>". We just want the first part
            sender = sender.split("<")[0]

            snippet = message.get('snippet')

            detailsList.append(
                {
                    'address': connection.get("address"),
                    'id': myId,
                    'date': date,
                    'unread': 'UNREAD' in labels,
                    'labels': labels,
                    'sender': sender,
                    'snippet': snippet,
                    'subject': subject
                })

    return detailsList


if __name__ == '__main__':
    tok = "d4d7aca543e0c5b96e795f71956c8323e05cad6c05791b069a9fb9444a530808"
    bil = get_email_details(2, tok)
    #hum = get_single_email("capstonespamtest@gmail.com",
                           #'16e1ffd1248982ac', tok)
