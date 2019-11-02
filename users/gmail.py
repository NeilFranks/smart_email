from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from .credsApi import add_account, retrieve_accounts
import email
import base64

# If modifying these scopes, delete the stored token.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def connect_new_account(app_token):
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    # get what you need from the profile
    service = build('gmail', 'v1', credentials=creds)
    profile = service.users().getProfile(userId='me').execute()
    address = profile.get('emailAddress')

    # call api to add creds to the associated user
    content = add_account(creds, address, app_token)

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

            # body = get_body(results.get('payload'))
            msg_str = base64.urlsafe_b64decode(results['raw'].encode('ASCII'))
            mime_msg = email.message_from_bytes(msg_str)
            messageMainType = mime_msg.get_content_maintype()
            if messageMainType == 'multipart':
                for part in mime_msg.get_payload():
                    if part.get_content_maintype() == 'text':
                        return part.get_payload()
                return ""
            elif messageMainType == 'text':
                return mime_msg.get_payload()
    return None


def get_email_details(address, n, app_token):
    '''
    Returns id, date (and time), from, and subject of the most recent n emails sent to the address.
    '''
    connections = retrieve_accounts(app_token)
    for connection in connections:
        if address == connection.get("address"):
            # get access to emails
            creds = connection.get("creds")
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().list(userId='me', maxResults=n).execute()
            labels = results.get('messages', [])

            detailsList = []
            if not labels:
                print('No labels found.')
            else:
                for label in labels:
                    message = service.users().messages().get(
                        userId='me', id=label['id'], format='metadata',
                        metadataHeaders=['Date', 'From', 'Subject']).execute()

                    # isolate the details
                    myId = message.get('id')
                    payload = message.get('payload')
                    headers = payload.get('headers')

                    for header in headers:
                        if header.get('name') == 'Date':
                            date = header.get('value')
                        if header.get('name') == 'From':
                            sender = header.get('value')
                        if header.get('name') == 'Subject':
                            subject = header.get('value')

                    detailsList.append(
                        {'id': myId, 'date': date, 'sender': sender, 'subject': subject})
            return detailsList
    return []


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


if __name__ == '__main__':
    tok = "452b8c9c861bb56d20df5d54b71931db8b04dbe9108441c1b35a10adb2e13d06"
    bil = get_email_details("neilcapstonetest@gmail.com", 2, tok)
    hum = get_single_email("neilcapstonetest@gmail.com",
                           '16e1ffd1248982ac', tok)
