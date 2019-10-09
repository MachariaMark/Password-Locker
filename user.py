import pyperclip
import string
import random

# result = pyfiglet.figlet_format("password locker", font = "doh" ) 
# print(result)

class User:
    """
    Class that generates new instances of users
    """
    user_log = []  # Empty user log

    def __init__(self, user_name, user_password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_name: New user name.
        '''

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        '''
        save_user method saves user objects into user_log
        '''

        User.user_log.append(self)


class Credentials:
    """
    Class that generates new instances of user Credentials
    """

    credentials_log = []  # Empty credentials log
    user_credentials_log = [] # Empty credential log

    def __init__(self, user_name, account_name, account_password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_password: New user_password.
            account_name = account_name.
            account_password = account_password.
        '''

        self.user_name = user_name
        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_log
        '''

        Credentials.credentials_log.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the user_log
        '''

        Credentials.credentials_log.remove(self)
    
    @classmethod
    def display_credentials(cls, user_name):
        '''
        method that returns list of credentials saved
        '''
        credentials_log = []
        for credential in cls.credentials_log:
            if credential.user_name == user_name:
                credentials_log.append(credential)
        return credentials_log
    
    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in a number and returns a credential that matches that account_name.

        Args:
            account_name: account_name to search for
        Returns :
            credential of person that matches the account_name.
        '''

        for credential in cls.credentials_log:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def copy_credential(cls, account_name):
        '''
        method that copies a credential details
        '''
        found_credential = Credentials.find_by_account_name(account_name)
        return pyperclip.copy(found_credential.credential)

    @classmethod
    def credential_exist(cls, account_name):
        '''
        Class method that checks if a credential exists
        '''
        for credential in cls.credentials_log  :
            if credential.account_name == account_name:
                return True
        return False