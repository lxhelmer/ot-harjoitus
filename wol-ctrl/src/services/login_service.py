from werkzeug.security import check_password_hash, generate_password_hash

class LoginService:
    def __init__(self, user_repo):
        self._users = user_repo

    def check_passwd(self, user, pswd):
        users = self._users.find_all()
        if user in users.keys():
            return check_password_hash(users[user], pswd)
