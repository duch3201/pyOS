
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

def LoadNeededFiles(username, RootDir):
    print("LoadNeededFiles")
    os.chdir(RootDir)
    print(os.getcwd())
    os.chdir("keys")
    FilesInKeysDir = os.listdir()
    print(os.listdir())
    with open("CurrentOS.vkey", 'r'):
        print(FilesInKeysDir)