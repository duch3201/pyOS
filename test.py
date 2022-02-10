import pathlib
import win32api
import os
drive = pathlib.Path.home().drive
#print(drive)

test = "Hello, World!"




#if test.endswith('H'):
   #print("Last character is 'H' ")
#else:
    #print("Last character is not 'H' ")
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print (drives)

string = 'This is a string'
print(drives[0])
print(drives[1])
print(drives[2])

if test[-10] == 'H':
   print("Last character is 'h' ")