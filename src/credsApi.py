import codecs
import json
import pickle
import requests


def add_account(creds, address, app_token):
    '''
    This is a POST method, used for saving new creds to the database for the associated user.
    User is authenticated by the app_token they obtain upon logging into our app.
    Login can be done by POSTing username and password to http://127.0.0.1:8000/api/auth/login
    '''
    # TODO: do input validation on address (needs to be an email address)
    stringCreds = codecs.encode(pickle.dumps(creds), "base64").decode()
    response = requests.post('http://127.0.0.1:8000/api/et/', headers={
        'Authorization': "Token %s" % app_token}, json={'token': stringCreds, "address": address})
    return response


def modify_account(idx, creds, app_token):
    '''
    This is a PUT method, used for changing existing creds in the database for the associated user.
    User is authenticated by the app_token they obtain upon logging into our app.
    Login can be done by POSTing username and password to http://127.0.0.1:8000/api/auth/login
    '''
    stringCreds = codecs.encode(pickle.dumps(creds), "base64").decode()
    response = requests.put('http://127.0.0.1:8000/api/et/%s/' % idx, headers={
        'Authorization': "Token %s" % app_token}, json={'token': stringCreds})
    return response


def retrieve_accounts(app_token):
    '''
    This is a GET method, used for viewing all existing creds and addresses in the database for the associated user.
    User is authenticated by the app_token they obtain upon logging into our app.
    Login can be done by POSTing username and password to http://127.0.0.1:8000/api/auth/login
    '''
    response = requests.get('http://127.0.0.1:8000/api/et/',
                            headers={
                                'Authorization': "Token %s" % app_token})

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
