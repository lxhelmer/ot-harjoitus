import unittest
from user_repository import UserRepository
from db_connection import get_test_connection
from init_db import init_test_db

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        init_test_db()
        test_connection = get_test_connection()
        self.userRp = UserRepository(test_connection)

    def test_initial_repo_is_empty_dict(self):
        self.assertEqual(self.userRp.find_all(), {})

    def test_adding_user_works(self):
        self.userRp.create("user1","hash1111")
        self.assertEqual(self.userRp.find_all(),{"user1":"hash1111"})
