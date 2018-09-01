from flask_httpauth import HTTPBasicAuth
from tif.models.user_model import UserModel

auth = HTTPBasicAuth()

users = UserModel().find()

@auth.get_password
def get_pw(username):
    for user in users:
        user = user.to_dict()
        print(user)
        if username in user:
            return user.get(username)

    return None
