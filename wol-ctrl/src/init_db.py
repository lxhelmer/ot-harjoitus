from db_connection import get_database_connection, get_test_connection

def drop_tables(connection):
    """Delete user and device tables from the database."""
    cursor = connection.cursor()

    cursor.execute('''
                   DROP TABLE IF EXISTS users;
                   ''')
    cursor.execute('''
                   DROP TABLE IF EXISTS devices;
                   ''')
    connection.commit()

def create_tables(connection):
    """Create user and device tables.
    Arg:
        connection: database connection
    """
    create_user_table(connection)
    create_device_table(connection)

def create_user_table(connection):
    """Create user table with the 
    specified fields.

    Arg:
        connection: database connection
    """
    connection.cursor().execute('''
                   CREATE TABLE users (
                       username text primary key,
                       hash text
                    );
                   ''')
    connection.commit()

def create_device_table(connection):
    """Create device table with the 
    specified fields.

    Arg:
        connection: database connection
    """
    connection.cursor().execute('''
                   CREATE TABLE devices (
                       id   INTEGER PRIMARY KEY,
                       name TEXT,
                       user TEXT,
                       mac TEXT,
                       ip TEXT
                       );
                   ''')
    connection.commit()

def init_db():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    init_test_db()

def init_test_db():
    test_connection = get_test_connection()

    drop_tables(test_connection)
    create_tables(test_connection)


if __name__ == "__main__":
    init_db()
