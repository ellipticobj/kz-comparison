import json
import logging
from sys import exit
from classes import *
from funcs import *

print("KZ stats tool")

debug = input("enter to start: ").lower().strip()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='app.log',
                    filemode='a')

if debug == 'verbose' or debug == 'v' or debug == 'debug' or debug == 'd':
    consolehandler = logging.StreamHandler()
    consolehandler.setLevel(logging.DEBUG)
    consolehandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(consolehandler)

try:
    with open('models.json', 'r+') as models:
        rawcont = models.readlines()
        cont = json.load(rawcont)
except FileNotFoundError:
    logging.error("models.json not found")
    print("models.json not found. Did you rename it?")
    makenewmodelsjson = input("Make empty models.json? [y/N] ").strip().lower()
    if makenewmodelsjson == 'y':
        open('models.json', 'w+')
        logging.info("empty models.json created")
        logging.info("continuing with empty models.json")
    else:
        logging.warning("exiting program due to error: FileNotFoundError")
        exit()

while True:
    choice = input('''
1. view stats
2. compare stats
3. exit
> ''').strip()
    
    if choice == '1':
        view()
    elif choice == '2':
        compare()
    elif choice == '3':
        break
    else:
        print("invalid choice")

   
print("exiting...", end='')
print('quit')