import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row

test_connection = sqlite3.connect(os.path.join(dirname, "..", "data", "test_database.sqlite"))
test_connection.row_factory = sqlite3.Row

def get_database_connection():
    """Delivers database connection for application
    to use
    """
    return connection

def get_test_connection():
    """Delivers database connection for test
    usage
    """
    return test_connection
