import unittest
from services.login_service import LoginService
from user_repository import UserRepository

class TestLoginService(unittest.TestCase):
    def setUp(self):
        self.userRp = UserRepository() 
        self.loginServ = LoginService(self.userRp)

    def test_login_fails_with_no_users(self):
        ret = self.loginServ.check_passwd("admin", "admin")
        self.assertEqual(ret, False)

    def test_login_works_with_default(self):
        self.userRp.create(
            "admin",
            "scrypt:32768:8:1$w5gDLWpvraPNqc4Q$0105f60696e65049ff24cac16668b538426572715fb52f494644fbca311e0cb68b2f6957b6c9c74ad7a8593180f722e968879e80f07772b9f9b36a6dd20c6b8e"
            )
        ret = self.loginServ.check_passwd("admin", "admin")
        self.assertEqual(ret, True)




        


