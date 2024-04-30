class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        rows = self._read()
        users = {}
        for row in rows:
            users[row["username"]] = row["hash"]
        return users

    def create(self, username, usr_hash):
        users = self.find_all()
        if username not in users.keys():
            users[username] = usr_hash
            self._write(username, users[username])
            return username
        return ""

    def _read(self):
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM users''')
        rows = cursor.fetchall()
        return rows

    def _write(self, username, hash):
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO users 
                       (username, hash) VALUES (?,?)''',
                       (username, hash))
        self._connection.commit()

