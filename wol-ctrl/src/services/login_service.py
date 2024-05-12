from werkzeug.security import check_password_hash

class LoginService:
    """Class for handling the loging functionality.
    """
    def __init__(self, user_repo):
        self._users = user_repo

    def check_passwd(self, username_string, pswd):
        if username_string == "" or pswd == "":
            return False, 0
        users = self._users.find_all()
        for user in users:
            if user.username == username_string:
                if check_password_hash(user.hash, pswd):
                    return True, user.id
        return False, 0
