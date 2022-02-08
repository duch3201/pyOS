# import all the needed modules
import os
import sys
import getpass
import hashlib
import platform
import time
import uuid
import bcrypt
import logging
import random
import secrets  
import cryptocode
from random import seed
from random import random

print("Welcome to pyOS setup")
print("let's start by creating a user account")

Username = input("Username: ")
Password = getpass.getpass("Password: ")

os.chdir("..")
os.chdir("etc/passwrd")

try:
    os.chdir(Username)
    boolFileExists = True
except FileNotFoundError:
    boolFileExists = False

if boolFileExists == True: 
    print("A user folder with this name already exists!")
    sys.exit()
if boolFileExists == False:
    os.mkdir(Username)
    os.chdir(Username)
    with open("passwrd", 'w') as passwrd_file:
        # seed random number generator
        seed(1)
        # generate some random numbers
        RanCode = random()
        passwrd = cryptocode.encrypt(Password, str(RanCode))
        passwrd_file.write(passwrd)
        print(passwrd)   
    with open("code" , 'w') as code_file:
        code_file.write(str(RanCode))
    print("User account created")








#os.chdir(Username)
#Security_Token = secrets.token_urlsafe(16)
#salt = bcrypt.gensalt()
#Hashed_Password = Password
#Hashed_Password = bcrypt.hashpw(Security_Token.encode(), salt)
#with open("passwrd", 'w+b') as Passwrd_file:
 #   Passwrd_file.write(bcrypt.hashpw(Security_Token.encode(), salt))
#with open("code", 'w') as security_token:
 #   security_token.write(Security_Token)
#with open("salt", 'w') as salt_file:
 #   salt_file.write(salt)
#print("User account created")
#print(Hashed_Password)
#print(salt)