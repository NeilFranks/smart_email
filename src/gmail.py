from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from credsApi import retrieve_creds

# If modifying these scopes, delete the stored token.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    creds = None
    # The stored token stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # r = requests.get('http://127.0.0.1:8000/api/et/',
    #                  headers={'Authorization': 'Token 11997d9aed82385d4811947006edd0ea3af2e9a75881ed5d57da13285b9aa42c'})
    # if r.content:
    #     credString = r.content[0]
    #     with tempfile.NamedTemporaryFile() as temp:
    #         temp.write(credString)
    #         creds = pickle.load(temp)
    #         temp.close()

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    tok = "05d4d54fa8b5747eb509c4a29e0a6d8a21dd8a963153b7642493af3d3e2d1f84"
    buh = retrieve_creds(tok)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId='me').execute()
    labels = results.get('messages', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            message = service.users().messages().get(
                userId='me', id=label['id']).execute()
            """
            print(message)
            print("")"""


if __name__ == '__main__':
    main()
    print("done")
