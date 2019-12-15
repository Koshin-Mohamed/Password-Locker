import string
import random

class Credential:

    """
    A class to generate new password credentials given a username.
    """

    credential_list = [] # Empty credential list

    def __init__(self, account_username, account_password):

        """[summary]
          __init__ method that helps us define properties for our objects.

        Args:
          account_username = username for existing username.
          account_password = password for existing account.
        """

        self.account_username = account_username
        self.account_password = account_password

    def save_credential(self):

        """
          save_credential method saves credential objects into credential_list
        """

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_user method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def gen_pass(cls, size = 8, char = string.ascii_letters + string.digits):

        """
          gen_pass method generates password objects into credential_list
        """
        return ''.join(random.choice(char) for i in range(size))