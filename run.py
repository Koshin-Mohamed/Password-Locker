#!/usr/bin/env python3.8

from user import User
from credential import Credential
import string
import random

def create_user(username, passoword):
    '''
    Function to create a new users
    '''
    new_user = User(username, passoword)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def find_user(username, password):
    '''
    Function that finds a credential by account type
    '''
    return User.login(username, password)

def create_credential(account_type, account_username, account_passoword):
    '''
    Function to create a new credentials
    '''
    new_user_cred = Credential(account_type, account_username, account_passoword)
    return new_user_cred

def generate_password(length = 8, char = string.ascii_letters + string.digits):
    '''
    function that generates password for the user
    '''
    return ''.join(random.choice(char) for i in range(length))

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_account_credentials(account_type):
    '''
    Function that finds a credential by account type
    '''
    return Credential.find_by_account_type(account_type)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

