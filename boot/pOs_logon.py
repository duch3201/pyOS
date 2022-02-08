from ast import Load
import sys
import os
import zlib
import platform
import getpass
import time
import uuid
import bcrypt
import logging
import hashlib
import cryptocode
from random import seed
from random import random
from Loader import LoadNeededFiles

print("pOs_logon.py")

os.chdir("..")
RootDir = os.getcwd()
os.chdir("etc\passwrd")


# these two function checks if the user is logged in
def LoginCheck():
  os.chdir(RootDir)
  os.chdir("keys")
  with open("IsLoggedIn.vkey", "r") as Vkey:
    Vkey = Vkey.read()
    if Vkey == "1":
      # if the value in IsLoggedIn.vkey is 1, sets the global variable IsLoggedIn to True
      IsLoggedIn = True
    else:
      IsLoggedIn = False

def SetNewVkey(boolResetIsLoggedInKey):
  os.chdir(RootDir)
  os.chdir("keys")
  with open("IsLoggedIn.vkey", "w") as NvKey:
    if boolResetIsLoggedInKey == True:
      NvKey.write("0")
    else:
      NvKey.write(str("1"))
  return


#this is the login function
def login():

  global IsLoggedIn
  IsLoggedIn = ""

  LoginCheck()

  if IsLoggedIn == True:
    print("You are already logged in.")
    #global boolResetIsLoggedInKey
    #boolResetIsLoggedInKey = True
    # this calls the SetNewVkey function to reset the IsLoggedIn.vkey file to 0
    #SetNewVkey(boolResetIsLoggedInKey)

  os.chdir(RootDir)
  os.chdir("etc\passwrd")
  username = input("Username: ")
  password = getpass.getpass("Password: ")

  try: 
    os.chdir(username)
  except FileNotFoundError:
    print("invalid username")

  with open("passwrd", 'r') as passwrd_file:
    passwrd = passwrd_file.read()
    with open("code", 'r') as code_file:
      code = code_file.read()
      passwrd = cryptocode.decrypt(passwrd, code)
      if passwrd == password:
        print("welcome")
        IsLoggedIn = True
        #SetNewVkey(boolResetIsLoggedInKey)
        LoadNeededFiles(username, password, RootDir)
      else:
        print("invalid password")

login()
































#logging.basicConfig(filename='pOS.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.info('System started, reached pOs_logon')

#os.chdir("etc\passwrd")

#username = input("Username: ")
#try:
 # os.chdir(username)
#except FileNotFoundError:
 # print("User account not found")
  #sys.exit()

#with open("code", 'r') as security_token:
 # security_token = security_token.read()

#with open("salt", 'r') as salt_file:
 # salt = salt_file.read()
  #salt.encode()
  
#password = getpass.getpass("Password: ")
#password = hashlib.md5(password.encode('utf-8')).hexdigest()
#password.encode()
#password = bcrypt.hashpw(security_token.encode(), salt)
#print(password)
#os.chdir("etc")
#os.chdir("passwrd")
#try:
 #  os.chdir(username)
  # os.getcwd()
#except FileNotFoundError:
 #  print("User not found")
  # sys.exit()
   

#with open("passwrd", 'r') as Passwrd_file:
  # compare_passwords = Passwrd_file.read()
  # print(compare_passwords)
   #print(Passwrd_file.read())
   #print(password)
   #if password == compare_passwords:
    #  print("Login successful")