class User:

    """
    A class to create new instances of a user
    """

    user_list = [] # Empty user list

    def __init__(self,username, password):

        """[summary]
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password : New user password.
        """

        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)



