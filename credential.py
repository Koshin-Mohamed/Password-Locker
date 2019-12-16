import string
import random

class Credential:

    """
    A class to generate new password credentials given a username.
    """

    credential_list = [] # Empty credential list

    def __init__(self, account_type, account_username, account_password):

        """[summary]
          __init__ method that helps us define properties for our objects.

        Args:
          account_type = account name of existing or future app
          account_username = username for existing username.
          account_password = password for existing account.
        """

        self.account_type = account_type
        self.account_username = account_username
        self.account_password = account_password

    def save_credential(self):

        """
          save_credential method saves credential objects into credential_list
        """

        Credential.credential_list.append(self)
        Credential.gen_pass()

    def delete_credential(self):

        '''
        delete_user method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials returns the credentials list
        '''
        return cls.credential_list

    @classmethod
    def gen_pass(cls, size = 8, char = string.ascii_letters + string.digits):

        """
          gen_pass method generates password objects into credential_list
        """
        return ''.join(random.choice(char) for i in range(size))