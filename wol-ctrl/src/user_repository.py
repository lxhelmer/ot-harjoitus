class UserRepository:
    def __init__(self):
        self._users = {"admin":"scrypt:32768:8:1$w5gDLWpvraPNqc4Q$0105f60696e65049ff24cac16668b538426572715fb52f494644fbca311e0cb68b2f6957b6c9c74ad7a8593180f722e968879e80f07772b9f9b36a6dd20c6b8e"}

    def find_all(self):
        return self._read()

    def create(self, username, usr_hash):
        users = self.find_all()
        if username not in users.keys():
            users[username] = usr_hash
            self._write(users)
            return username
        return ""

    def _read(self):
        return self._users

    def _write(self, users):
        self._users = users
