import json
import logging
from sys import exit
from classes import *
from funcs import *

'''
overcomplicated program for a problem no one has
'''

print("KZ stats tool")

# debug?
debug = input("enter to start: ").lower().strip()

# logging init
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='app.log',
                    filemode='a')
if debug == 'verbose' or debug == 'v' or debug == 'debug' or debug == 'd':
    consolehandler = logging.StreamHandler()
    consolehandler.setLevel(logging.DEBUG)
    consolehandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(consolehandler)


parsejson("iems")
parsejson("bluetooth")
parsejson("dacs")

while True:
    choice = input('''
1. view stats
2. compare stats
3. add item to json
3. exit
> ''').strip()
    
    if choice == '1':
        view(cont)
    elif choice == '2':
        compare(cont)
    elif choice == '3':
        break
    else:
        print("invalid choice")

   
print("exiting...", end='')
print('quit')