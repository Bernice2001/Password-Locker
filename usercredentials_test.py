import unittest
from usercredentials import User,Credentials
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Bernice','Bernice019')
    def test_init(self):
        self.assertEqual(self.new_user.username,'Bernice')
        self.assertEqual(self.new_user.password,'Bernice019')    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials('Twitter','Bernice','Bernice019')
    def  test_init(self):
        self.assertEqual(self.new_credentials.account,'Twitter')
        self.assertEqual(self.new_credentials.username,'Bernice')
        self.assertEqual(self.new_credentials.password,'Bernice019')
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1) 

    def tearDown(self):
        Credentials.credentials_list = []

    def test_save_multiple_accounts(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Instagram','Bernice','Bernice019')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)           
if __name__ == '__main__':
    unittest.main() 
