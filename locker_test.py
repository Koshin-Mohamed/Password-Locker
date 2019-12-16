import unittest
import random
import string

from user import User
from credential import Credential

class TestUsers(unittest.TestCase):

    """
    Test class that defines test cases for the User and C class.

    Args:
        unittest.TestCase: TestCase class that helps in creating test classes.

    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Koshin","Pa$$w0rd") # create contact object
        self.new_credential = Credential("Instagram", "Kdot", "Section80") #create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Koshin")
        self.assertEqual(self.new_user.password,"Pa$$w0rd")

        self.assertEqual(self.new_credential.account_type, "Instagram")
        self.assertEqual(self.new_credential.account_username,"Kdot")
        self.assertEqual(self.new_credential.account_password,"Section80")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        Credential.credential_list = []

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() #save new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        """
        test_save_multiple_user test to check if we can save multiple user
        object to the user_list
        """
        self.new_user.save_user()
        test_user = User("tweeter", "Test12") #new user

        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_credential(self):
        """
        test_delete_user test case to test if the user object is deleted from
        the credential list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "tweeter", "Test12") #new user
        test_credential.save_credential()

        self.new_credential.delete_credential() #delete new user
        self.assertEqual(len(Credential.credential_list),1)







if __name__ == '__main__':
    unittest.main()

