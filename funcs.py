import logging
import json


def parsejson(type):
    # opens models.json and reads content and decodes it woaow
    try:
        with open(f'{type}.json', 'r+') as models:
            rawcont = models.readlines()
            cont = json.load(rawcont)
    except FileNotFoundError:
        logging.error(f"{type}.json not found")
        print(f"{type}.json not found. Did you rename it?")
        makenewjson = input(f"Make empty {type}.json? [y/N] ").strip().lower()
        if makenewjson == 'y':
            open(f'{type}.json', 'w+')
            logging.info(f"empty {type}.json created")
            logging.info(f"continuing with empty {type}.json")
        else:
            logging.warning(f"exiting program due to error: FileNotFoundError")
            exit()
    except json.JSONDecodeError:
        logging.error(f"Error decoding {type}.json")
        print(f"Error decoding {type}.json. Is the file empty or corrupted?")
        exit()
    return cont

def view(cont):
    choice = input("input models to view: ").lower().strip()
    
    pass

def compare(cont):
    pass

def add(cont):
    typetoadd = input("input type to add [e/b/d/q]: ").strip().lower()
    while typetoadd not in ['e','b','d','q']:
        typetoadd = input("input type to add [e/b/d/q]: ").strip().lower()
    name = input("input model name: ")
    if typetoadd == 'e':
        pass
    # TODO
