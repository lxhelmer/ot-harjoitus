import unittest
from services.login_service import LoginService
from repositories.user_repository import UserRepository
from db_connection import get_test_connection

class TestLoginService(unittest.TestCase):
    def setUp(self):
        self.userRp = UserRepository(get_test_connection()) 
        self.loginServ = LoginService(self.userRp)

    def test_login_fails_with_no_users(self):
        ret = self.loginServ.check_passwd("admin", "admin")
        self.assertEqual(ret, (False,0))

    def test_login_works_with_default(self):
        self.userRp.create("admin","admin")
        ret = self.loginServ.check_passwd("admin", "admin")
        self.assertEqual(ret, (True, 1))



        


