from werkzeug.security import generate_password_hash
from classes.objects import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        rows = self._read()
        users = []
        for row in rows:
            users.append(User(row["id"],row["username"],row["hash"]))
        return users

    def create(self, username, pws):
        users = self.find_all()
        if username not in list(map(lambda x: x.username, users)):
            hash  = generate_password_hash(pws)
            self._write(username, hash)
            return username
        return ""

    def _read(self):
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM user''')
        rows = cursor.fetchall()
        return rows

    def _write(self, username, hash):
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO user
                       (username, hash) VALUES (?,?)''',
                       (username, hash))
        self._connection.commit()
