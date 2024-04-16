import unittest
from user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.userRp = UserRepository()

    def test_initial_repo_is_empty_dict(self):
        self.assertEqual(self.userRp.find_all(), {})

    def test_adding_user_works(self):
        self.userRp.create("user1","hash1111")
        self.assertEqual(self.userRp.find_all(),{"user1":"hash1111"})
