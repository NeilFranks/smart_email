import base64


def get_body(email_message):

    for part in email_message.get('parts'):
        try:
            body = part.get('body')
            data = body.get('data')
            text = base64.b64decode(data+'=')
            return text
        except:
            pass
        return None
