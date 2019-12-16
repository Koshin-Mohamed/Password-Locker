import unittest

from user import User
from credential import Credential

class TestUsers(unittest.TestCase):

    """
    Test class that defines test cases for the User login and signups.
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Koshin","Pa$$w0rd") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Koshin")
        self.assertEqual(self.new_user.password,"Pa$$w0rd")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() #save new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        """
        Tests to check if we can store multiple accounts
        """
        self.new_user.save_user()
        test_user = User("tweeter", "Test12") #new user

        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_user_exists(self):
        '''
        test to check if users username and password already exists.
        '''

        self.new_user.save_user()
        test_user = User("Drake","scorpion") # new user
        test_user.save_user()

        user_exists = User.login("Drake","scorpion")

        self.assertTrue(user_exists)

class TestCredential(unittest.TestCase):

    '''
    Test class that enables users to create, view, and delete their credentials
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("IG", "Kdot", "Section80") #create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_type, "IG")
        self.assertEqual(self.new_credential.account_username,"Kdot")
        self.assertEqual(self.new_credential.account_password,"Section80")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
        the credentail list
        '''
        self.new_credential.save_credential() #save new user
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        """
        Tests to check if we can store multiple credential
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook", "JCole", "ForestHillDrive") #new user
        test_credential.save_credential()

        self.assertEqual(len(Credential.credential_list),2)

    def test_find_credential(self):
        '''
        test enables user find the password of a specific account
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","JCole","ForestHillDrive")
        test_credential.save_credential()

        find_credential = Credential.find_by_account_type("Facebook")
        self.assertEqual(find_credential.account_password,test_credential.account_password)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

    def test_delete_credential(self):
        """
        test_delete_user test case to test if the user object is deleted from
        the credential list
        """
        self.new_credential.save_credential()
        self.new_credential.del_credential() #delete new user
        self.assertEqual(len(Credential.credential_list),0)

if __name__ == '__main__':
    unittest.main()

