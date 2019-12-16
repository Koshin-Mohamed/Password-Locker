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
    def find_by_account_type(cls,account_type):
        '''
        this method returns the password of the account type entered
        '''
        for credentials in cls.credential_list:
            if credentials.account_type == account_type:
                return credentials