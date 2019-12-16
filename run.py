#!/usr/bin/env python3.8

from user import User
from credential import Credential

def create_user(username, passoword):
    '''
    Function to create a new users
    '''
    new_user = User(username, passoword)
    return new_user

def create_credential(account_type, account_username, account_passoword):
    '''
    Function to create a new credentials
    '''
    new_user_cred = Credential(account_type, account_username, account_passoword)
    return new_user_cred

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

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

def find_user(username,password):
    '''
    Function that finds a user by username and returns the username
    '''
    return User.locate_user(username, password)

def check_existing_user(username, password):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username, password)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

