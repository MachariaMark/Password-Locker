import unittest  # Importing the unittest module
from user import User  # Importing the user class
from user import Credentials # Importing the Credentials class
import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_log = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Mark", "12345")  # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "Mark")
        self.assertEqual(self.new_user.user_password, "12345")
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user log
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_log), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_log
        '''
        self.new_user.save_user()
        test_user = User("Test", "12345")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_log), 2)

class Test_Credentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_log = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credential = Credentials("Hirani", "Hotmail", "09876")


    def test__init__(self):
        '''
        Test case to check if creation of credential instances is properly done.
        '''
        self.assertEqual(self.new_credential.user_name, "Hirani")
        self.assertEqual(self.new_credential.account_name, "Hotmail")
        self.assertEqual(self.new_credential.account_password, "09876")


if __name__ == '__main__':
    unittest.main()
 