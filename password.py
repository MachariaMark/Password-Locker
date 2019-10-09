#!/usr/bin/env python3.6
import pyperclip
from user import User 
from user import Credentials
import random

def create_user(user_name, password):
    '''
    Function to create a new contact
    '''
    new_user = User(user_name, password)
    return new_user


def save_user(User):
    '''
    Function to save user
    '''
    User.save_user()


def create_credential(user_name ,account_name , password):
    '''
    Function that creates new credentials.
    '''
    new_credential = Credentials(user_name ,account_name , password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential.
    '''
    Credentials.save_credentials(credential)

def display_credentials(user_name):
    '''
    Function that returns saved credentials
    '''
    return Credentials.display_credentials(user_name)

def delete_credentials(Credentials):
    '''
    Function that deletes a credential
    '''
    Credentials.delete_credential()


def find_by_account_name(account_name):
    '''
    Function that finds by account name.
    '''
    return Credentials.find_by_account_name(account_name)

# def generate_password(self):
#     return Credentials.passGen(self)


def copy_credential(account_name):
    '''
    Function that copies credentials details.
    '''
    return Credentials.copy_credential(account_name)

def delete_credential(credential):
    '''
    Function that deletes credentials.
    '''
    credential.delete_credential()

def check_credentials(account_name):
    '''
    Function that checks if a credential exists.
    '''
    return Credentials.credential_exist(account_name)\


def main():
    print("Hello Welcome to Password locker.")
    user_name = input("Enter username >>")
    password = input("Enter password >>")


    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : \n ac - Add new credentials, \n dc - display credentials, \n fc -find a credentials, \n ex -exit the app")

            short_code = input().lower()
            Credentials=""
            if short_code == 'ac':
                print("New credentials")
                print("-"*10)

                print("User name ...")
                user_name = input('>>')

                print("Account ...")
                account_name = input('>>')

                print("Password ...")
                print('\n')
                print("Would you like to generate a password ? (y/n)")
                answer = input('>>')
                if answer == 'y':
                    print("Enter length of the password :")
                    length = int (input('>>'))
                    chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
                    password = ''

                    for _ in range (length):
                        password += random.choice(chars)    
                    print (password)
                    return password
                    
                elif answer == 'n':
                    print("Enter your preferred password :")
                    password = input('>>')
                # create and save new contact.
                save_credential(create_credential(user_name, account_name, password))
                print('\n')
                print(f"New Credential {user_name} {account_name} created")
                print('\n')   

            elif short_code == 'dc':

                if display_credentials(user_name):
                    print("Here is a list of all your credentials")
                    print('\n')

                    for Credentials in display_credentials(user_name):
                        print(
                            f"{Credentials.user_name} {Credentials.account_name} .....{Credentials.account_password}")

                    print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

            elif short_code == 'fc':

                print("Enter the account you want to search for")

                search_account = input()
                if check_credentials(search_account):
                    search_account = find_by_account_name(search_account)
                    print(f"{search_account.user_name} {search_account.user_name}")
                    print('-' * 20)

                    print(f"User name.......{search_account.user_name}")
                    print(f"Account name.......{search_account.account_name}")
                else:
                    print("That credential does not exist")

            elif short_code == "ex":
                print("See ya .......")
                break
            else:
                print("I didn't quite get that. Please do use the short codes")


if __name__ == '__main__':

    main()