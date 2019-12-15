import unittest
from user import User

class TestUsers(unittest.TestCase):

    """
    Test class that defines test cases for the User class.

    Args:
        unittest.TestCase: TestCase class that helps in creating test classes.

    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("SnapChat","koshin.moh@gmail.com","k0sh1n","Pa$$w0rd") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account_type,"SnapChat")
        self.assertEqual(self.new_user.email,"koshin.moh@gmail.com")
        self.assertEqual(self.new_user.username,"k0sh1n")
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

    def test_delete_user(self):
        """
        test_delete_user test case to test if the user object is deleted from
        the user list
        """
        self.new_user.save_user()
        test_user = User("Twitter", "test@test.com", "tweeter", "Test12")
        test_user.save_user()

        self.new_user.delete_user() #delete new user
        self.assertEqual(len(User.user_list),1)







if __name__ == '__main__':
    unittest.main()

