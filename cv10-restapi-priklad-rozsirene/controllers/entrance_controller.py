from flask import Blueprint, request, jsonify
from models import users_model
from helpers import jwt_helper
entrance_blueprint = Blueprint('entrance', __name__,)


@entrance_blueprint.route('/login', methods=['POST'])
def login_user():
    user_data = request.json
    user = users_model.get_user_by_email(user_data['email'])
    if len(user) == 0:
        return jsonify("User not found"), 404
    if not users_model.composer_user_password(user_data['email'],user_data['password']):
        return jsonify("User password is incorrect"), 403
    resutl = {
        "user": user,
        "jwt" : jwt_helper.encode_auth_token(user_data['email'])
        }
    return jsonify(resutl), 200


@entrance_blueprint.route('/registration', methods=['POST'])
def registration():
    user_data = request.json
    return jsonify(users_model.create_user(user_data['username'], user_data['email'],user_data['password'])), 201


@entrance_blueprint.route('/all-users')
def get_all_users():
    return jsonify(users_model.get_all_user()), 200

# @entrance_blueprint.route('/logout')
# def logout_user():
#     return 'login url  index route'

