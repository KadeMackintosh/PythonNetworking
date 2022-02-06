import jwt
from flask import jsonify, request
from helpers import jwt_helper

def is_auth():
    try:
        print("is_auth")
        print(request.headers.get('Authorization'))
        print(request.headers.get('Authorization')[7:])
        # print(jwt_helper.decode_auth_token(request.headers.get('Authorization')[7:]))
        request.user = jwt_helper.decode_auth_token(request.headers.get('Authorization')[7:])
    except Exception as e:
        return  str(e), 401


def is_admin():
    print("is_admin")
    print(request.user)