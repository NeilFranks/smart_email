def GenerateOAuth2String(username, access_token, base64_encode=True):
    """Generates an IMAP OAuth2 authentication string.

    See https://developers.google.com/google-apps/gmail/oauth2_overview

    Args:
      username: the username (email address) of the account to authenticate
      access_token: An OAuth2 access token.
      base64_encode: Whether to base64-encode the output.

    Returns:
      The SASL argument for the OAuth2 mechanism.
    """
    auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, access_token)
    if base64_encode:
        auth_string = base64.b64encode(auth_string)
    return auth_string


def TestImapAuthentication(user, auth_string):
    """Authenticates to IMAP with the given auth_string.

    Prints a debug trace of the attempted IMAP connection.

    Args:
      user: The Gmail username (full email address)
      auth_string: A valid OAuth2 string, as returned by GenerateOAuth2String.
          Must not be base64-encoded, since imaplib does its own base64-encoding.
    """
    print
    imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')
    imap_conn.debug = 4
    imap_conn.authenticate('XOAUTH2', lambda x: auth_string)
    imap_conn.select('INBOX')
