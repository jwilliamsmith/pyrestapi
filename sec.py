from werkzeug.security import safe_str_cmp
from models.user import UserModel


def auth(un, pw):
    user = UserModel.find_by(('username', un))
    if user and safe_str_cmp(user.password, pw):
        return user

def ident(payload):
    user_id = payload['identity']
    return UserModel.find_by(('id', user_id))