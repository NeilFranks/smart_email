from __future__ import print_function

import base64
import os.path
import pickle

import dateutil.parser as parser
from apiclient import discovery
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = discovery.build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    user_id = 'me'
    final_list = []

    response = service.users().messages().list(userId=user_id).execute()
    mssg_list = response['messages']
    print("Total messages in inbox: ", str(len(mssg_list)))

    for mssg in mssg_list:
        temp_dict = {}
        m_id = mssg['id']  # get id of individual message
        message = service.users().messages().get(
            userId=user_id, id=m_id).execute()  # fetch the message using API
        payld = message['payload']  # get payload of the message
        headr = payld['headers']  # get header of the payload

        # getting the from
        for _ in headr:
            if _['name'] == 'From':
                msg_from = _['value']
                temp_dict['From'] = msg_from
            else:
                pass

        # getting the to
        for _ in headr:
            if _['name'] == 'To':
                msg_to = _['value']
                temp_dict['To'] = msg_to
            else:
                pass

        # getting the date
        for _ in headr:
            if _['name'] == 'Date':
                msg_date = _['value']
                date_parse = (parser.parse(msg_date))
                m_date = (date_parse.date())
                temp_dict['Date'] = str(m_date)
            else:
                pass

        # getting the Subject
        for _ in headr:
            if _['name'] == 'Subject':
                msg_subject = _['value']
                temp_dict['Subject'] = msg_subject
            else:
                pass

        temp_dict['Snippet'] = message['snippet']  # fetching message snippet

        try:
            # Fetching message body
            # print(payld)
            data = payld['parts'][0]['body']['data']
            # print('data : ', data)
            # decoding from Base64 to UTF-8
            clean_one = data.replace("-", "+")
            # decoding from Base64 to UTF-8
            clean_one = clean_one.replace("_", "/")
            # decoding from Base64 to UTF-8
            clean_two = base64.b64decode(bytes(clean_one, 'UTF-8'))
            soup = BeautifulSoup(clean_two, "lxml")
            mssg_body = soup.body()
            # mssg_body is a readible form of message body
            # depending on the end user's requirements, it can be further cleaned
            # using regex, beautiful soup, or any other method
            temp_dict['Message_body'] = mssg_body
        except:
            pass

        # This will create a dictonary item in the final list
        final_list.append(temp_dict)
    print(final_list)
    print("Total messaged retrived: ", str(len(final_list)))


if __name__ == '__main__':
    main()
