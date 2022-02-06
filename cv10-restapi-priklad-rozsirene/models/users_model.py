users = [
    {
        "id":0,
        "username": "admin",
        "password": "admin",
        "email": "admin@admin.com",
    }
]


def get_user_by_email(email):
    result = []
    for user in users:
        if user['email'] == email:
            result.append(user)
    return result

def composer_user_password(email, passord):
    result = False
    for user in users:
        if user['email'] == email and user['password'] == passord:
            result = True
    return result


def create_user(username, password,email):
    new_user =     {
        "id": len(users),
        "username": username,
        "password": password,
        "email": email,
    }
    users.append(new_user)
    return new_user


def get_all_user():
    return users
