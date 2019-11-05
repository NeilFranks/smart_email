import codecs
import json
import os
import pickle
import requests


def add_account(creds, address, app_token):
    '''
    This is a POST method, used for saving new creds to the database for the associated user.
    User is authenticated by the app_token they obtain upon logging into our app.
    Login can be done by POSTing username and password to /api/auth/login
    '''
    # TODO: do input validation on address (needs to be an email address)
    stringCreds = codecs.encode(pickle.dumps(creds), "base64").decode()

    response = requests.post('%s/api/et/' % baseURL(), headers={
        'Authorization': app_token}, json={'creds': stringCreds, "address": address})
    content = json.loads(response.content)
    return content


def modify_account(idx, creds, app_token):
    '''
    This is a PUT method, used for changing existing creds in the database for the associated user.
    User is authenticated by the app_token they obtain upon logging into our app.
    Login can be done by POSTing username and password to /api/auth/login
    '''
    stringCreds = codecs.encode(pickle.dumps(creds), "base64").decode()
    response = requests.put('%s/api/et/%s/' % (baseURL(), idx), headers={
        'Authorization': app_token}, json={'creds': stringCreds})
    return response


def retrieve_accounts(app_token):
    '''
    This is a GET method, used for viewing all existing creds and addresses in the database for the associated user.
    User is authenticated by the app_token they obtain upon logging into our app.
    Login can be done by POSTing username and password to /api/auth/login
    '''
    response = requests.get('%s/api/et/' % baseURL(),
                            headers={
                                'Authorization': app_token})

    if response.status_code == 200:
        accountList = []
        content = json.loads(response.content)
        for entry in content:
            idx = entry.get("id")
            credsString = entry.get("creds")
            address = entry.get("address")
            try:
                creds = pickle.loads(codecs.decode(
                    credsString.encode(), "base64"))
                accountList.append(
                    {'id': idx, 'address': address, 'creds': creds})
            except ValueError as e:
                # TODO: IDK where this prints out to.. if it prints at all. Should log somehow
                print("creds '%s' could not be decoded" % credsString)
        return accountList
    return []


def baseURL():
    # in Procfile for heroku, BASE_URL should be set to `export BASE_URL=https://capstone-smart-email.herokuapp.com/`
    baseURL = os.environ['BASE_URL']
    if not baseURL:
        baseURL = 'http://127.0.0.1:8000'

    print("baseURL set to %s" % baseURL)
    return baseURL
