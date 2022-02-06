import jwt
import datetime
import configs.main_config


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, configs.main_config.APP.get("jwt_secret_key"))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise   Exception('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token. Please log in again.')

        
def encode_auth_token(userName):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': userName
        }
        return jwt.encode(
            payload,
            configs.main_config.APP.get("jwt_secret_key"),
            algorithm='HS256'
        ).decode('utf-8')
    except Exception as e:
        return e