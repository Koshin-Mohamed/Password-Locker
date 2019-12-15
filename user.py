class User:

    """
    A class to create new instances of a user
    """

    user_list = [] # Empty user list

    def __init__(self,account_type, email, username, password):

        """[summary]
        __init__ method that helps us define properties for our objects.

        Arguments:
            account_type: New user account type being saved.
            email : New user email.
            username: New user username.
            password : New user password.
        """

        self.account_type = account_type
        self.email = email
        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_contact(self):

        '''
        delete_contact method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


