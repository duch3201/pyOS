
import sys
import os
import zlib
import platform
import getpass
import time
import uuid
import logging
import cryptocode
import importlib
from random import seed
from random import random
from UserSpace import main

def LoadNeededFiles(username, password, RootDir):
    print("LoadNeededFiles")
    os.chdir(RootDir)
    print(os.getcwd())
    os.chdir("keys")
    FilesInKeysDir = os.listdir()
    print(os.listdir())
    with open("CurrentOS.vkey", 'r') as CurrentOS:
        CurrentOS = CurrentOS.read()
    with open("IsAuthenticated.vkey", 'r') as IsAuthenticated:
        IsAuthenticated = IsAuthenticated.read() 
    #load needed modules
    os.chdir(RootDir)
    os.chdir("modules")
    try:
        with open("SudoAuthentication.module", 'r') as SudoAuthenticationModule:
            SudoAuthenticationModule = SudoAuthenticationModule.read()
        with open("SystemShutdown.module", 'r') as SystemShutdown:
            SystemShutdown = SystemShutdown.read()
    except:
        print("An unexpected error has occurred while loading the modules.")
        print("The Operating System cannot safely continue.")
        print("To prevent further damage, pyOS will now shut down.")
        sys.exit()
    
    # temporarly add the modules to the boot directory
    os.chdir(RootDir)
    os.chdir("boot")
    try:
        with open("SudoAuthentication.py", 'w') as SudoAuthenticationModule:
            SudoAuthenticationModule.write(SudoAuthenticationModule)
        with open("SystemShutdown.py", 'w') as SystemShutdown:
            SystemShutdown.write(SystemShutdown)
    except:
        print("An unexpected error has occurred while moving the modules.")
        print("The Operating System cannot safely continue.")
        print("To prevent further damage, pyOS will now shut down.")
        sys.exit()
    #print(SudoAuthenticationModule)
    main(username, password, RootDir)