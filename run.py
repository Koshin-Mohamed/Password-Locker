#!/usr/bin/env python3.8

from user import User
from credential import Credential
import string
import random

def create_user(username, password):
    '''
    Function to create a new users
    '''
    new_user = User(username, password)
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

def create_credential(account_type, account_username, account_password):
    '''
    Function to create a new credentials
    '''
    new_user_cred = Credential(account_type, account_username, account_password)
    return new_user_cred

def gen_pass(length = 8, chars = string.ascii_letters + string.digits):
    '''
    function that generates password for the user
    '''
    return ''.join(random.choice(chars) for i in range(length))

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

def main():
    print('\n')
    print('Welcome to Password-Locker! An app to organize all of your online account logins and usernames.')
    print('-' * 100)
    print('\n')
    print('Please choose from the following options: CA to create an account or LO to login to and existing one.')
    print('\n')

    short_code = input().upper()
    print('\n')

    if short_code == 'CA':
            print('\n')
            print("Ok, let's create a new account")
            print('\n')
            print('Please select a username:')
            username = input()
            print('Please select a password:')
            password = input()
            print('\n')
            save_user(create_user(username,password))
            print(f'Hey {username}! your account is ready to go and, your password is {password}.')
            print('*' * 100)
            print('\n')

    elif short_code == 'LO':
              print('\n')
              print('Ok, please enter your login username:')
              username = input()
              print('Please enter your password:')
              password = input()
              print('\n')
              login = find_user(username,password)
              if find_user == login:
                    print(f'Hi {username}, Welcome back to your password locker.')
                    print('*' * 100)
                    print('\n')

    while True:
        print('\n')
        print("Now that you're logged in, use these short codes to manoeuver around \n CC - create a new credential,\n DC - display credentials, \n FC -find a credential,\n DEL -delete a credential,\n EX -exit credentials list \n")
        print('\n')
        short_code = input().upper()
        if short_code == 'CC':
              print('\n')
              print('Create Credential Account')
              print('\n')
              print('Type of account:')
              account_type = input().lower()
              print('Account username:')
              account_username = input()
              print('Would you like a password to be generated for you? Y/N')
              pass_option = input().upper()
              if pass_option == 'Y':
                      print('Enter preferred password length')
                      length = int(input())
                      account_password = gen_pass(length)
                      print(f'Your {account_type} password is {account_password}')
              elif pass_option == 'N':
                      print('Select an account password:')
                      account_password = input()
                      print(f'Your {account_type} account has successfully been created.')
              save_credential(create_credential(account_type, account_username, account_password))
              print('-' * 100)

        elif short_code == 'DC':
            if display_credentials():
                print('\n')
                print("Here's is a list of all of your credentials:")
                print('\n')
                for credential in display_credentials():
                    print(f'Account name: {credential.account_type} \nUsername: {credential.account_username} \nPassword: {credential.account_password}')
                    print('-' * 100)
            else:
                print('\n')
                print("Oops, it seems you don't have an account with us")

        elif short_code == 'FC':
            print('\n')
            print('Please enter the name of account you wish to search for:')
            print('\n')
            account_query = input().lower()
            if find_account_credentials(account_query):
                credential_query = find_account_credentials(account_query)
                print(f'Your {account_query} account  password is: {credential_query.account_password}.')
                print('-' * 100)


            else:
                print("Oops, it seems that account doesn't not exist.")

        elif short_code == 'DEL':
            print('\n')
            print('Please enter the account you want to delete:')
            print('\n')
            account_type = input().lower()
            if find_account_credentials(account_type):
                query = find_account_credentials(account_type)
                query.del_credential()
                print(f'Your {query.account_type} account has been deleted.')
                print('-' * 100)

            else:
                print('That account does not exist')

        elif short_code == 'EX':
            print("That's All Folks!")
            break

if __name__ == '__main__':
    main()