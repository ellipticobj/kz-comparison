import json
import logging
from sys import exit
from classes import *
from utils import *

'''
overcomplicated program for a problem no one has
'''

# TODO: LOGGING LOGGING LOGGING
# TODO: fill up the jsons
# TODO: better ui ux etc

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


parsejson("iem")
parsejson("bluetooth")
parsejson("dac")

while True:
    choice = input('''
1. view stats
2. add item to json
3. exit
> ''').strip()
    
    if choice == '1':
        while True:
            type = input("Input product type [iem/bluetooth/dac]: ").lower().strip()
            if type in {"iem", "bluetooth", "dac"}:
                break
            else:
                print("please input a proper product type")
                continue
        view(type)
    
    elif choice == '2':
        add()
    
    elif choice =='3':
        break
    else:
        print("invalid choice")

   
print("exiting...", end='')
print('quit')