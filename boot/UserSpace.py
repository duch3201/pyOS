from cmath import exp
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
import importlib
from random import seed
from random import random
#from pOs_logon import login

#IsLoggedIn = ""

#login()
#print("UserSpace.py")

#def LoadNeededFiles():
 #   print("LoadNeededFiles")

def main(username, password, RootDir):
    try:
        print("hello " + username + "!")
        os.chdir(RootDir)
        command = input(": ")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()