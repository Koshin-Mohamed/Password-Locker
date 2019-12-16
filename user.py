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

    @classmethod
    def auth_user(cls, username, password):

        """
        auth_user method checks if the user by username
        """
        for user in cls.user_list:
            if user.username == username and user.password == password:
                print("Login Successful")
                return user
            else:
                print("either the username or password is wrong")



