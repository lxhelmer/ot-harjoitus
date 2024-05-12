import unittest
from repositories.user_repository import UserRepository
from db_connection import get_test_connection
from init_db import init_test_db
from classes.objects import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        init_test_db()
        test_connection = get_test_connection()
        self.userRp = UserRepository(test_connection)

    def test_initial_repo_is_empty_dict(self):
        self.assertEqual(self.userRp.find_all(), [])

    def test_adding_user_works(self):
        self.userRp.create("user1","hash1111")
        users = self.userRp.find_all()
        self.assertEqual(len(self.userRp.find_all()),1)
        self.assertEqual(users[0].username,"user1")
