from werkzeug.security import generate_password_hash
from classes.objects import User

class UserRepository:
    """Class for managing user instances.

    Attributes:
        connection: Database connection instance
    """

    def __init__(self, connection):
        """Initialising constructor for class.
        Args:
            connection: database connection
        """
        self._connection = connection

    def find_all(self):
        """Returns all user instances from the db.

        Returns:
            Users: list of Device objects in the form.
            User(id,name,hash)
        """
        rows = self._read()
        users = []
        for row in rows:
            users.append(User(row["id"],row["username"],row["hash"]))
        return users

    def create(self, username, pws):
        """Add a new user object to the database.
        Arg:
            username: username as string
            pws: password as string
        Returns:
            Either username or empty string to
            depict failure
        """
        users = self.find_all()
        if username not in list(map(lambda x: x.username, users)):
            psw_hash  = generate_password_hash(pws)
            self._write(username, psw_hash)
            return username
        return ""

    def _read(self):
        """Handles the SQL query for getting user
        entries from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM user''')
        rows = cursor.fetchall()
        return rows

    def _write(self, username, psw_hash):
        """Handles the SQL query of adding a
        object to the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO user
                       (username, hash) VALUES (?,?)''',
                       (username, psw_hash))
        self._connection.commit()
