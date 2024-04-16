class UserRepository:
    def __init__(self):
        self._users = {}

    def find_all(self):
        return self._read()

    def create(self, username, hash):
        users = self.find_all()
        if username not in users.keys():
            users[username] = hash
            self._write(users)
            return username
        return ""

    def _read(self):
        return self._users

    def _write(self, users):
        self._users = users

