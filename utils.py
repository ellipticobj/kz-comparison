import logging
import json
from classes import *

ports = ["2.5", "3.5", "4.4"]

def parsejson(type):
    # opens type.json and reads content and decodes it woaow
    try:
        with open(f'{type}.json', 'r+') as file:
            cont = json.load(file)
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

def getpresentinput(prompt: str = "Input: "):
    while True:
        inp = input(prompt).strip()
        if inp:
            break
        else:
            print("Please input something")
    return inp

def gettypeinput(prompt:str = "Input: ", type:str = "int"):
    if type == "int" or type == "integer":
        while True:
            inp = getpresentinput(prompt).strip()
            try:
                inp = int(inp)
                break
            except:
                print("Please input an integer")
        return inp
            
    elif type == "float":
        while True:
            inp = getpresentinput(prompt).strip()
            try:
                inp = float(inp)
                break
            except:
                print("Please input a float.")
        return inp
    
    elif type == "str" or type == "string":
        return input(prompt)
    
    elif type == "bool" or type == "boolean":
        while True:
            inp = getpresentinput(prompt).strip().lower()
            if inp not in {"true","false"}:
                print("Please input true or false. ")
                continue
            break
        
        if inp == "true":
            return True
        elif inp == "false":
            return False
        
    elif type == "port":
        while True:
            inp = getpresentinput(prompt).strip().lower()
            if inp not in set(ports):
                print(f"Please input one of the supported ports: {ports}")
                continue
            break
    
    else:
        raise ValueError(f"Unsupported type {type}")

def getmodel(type):
    while True:
        choice = input("input models to view or help to show available models: ").strip()
        
        content = parsejson(type)
        
        try:
            if choice == "help":
                print(f"Models: {content.keys()}")
                logging.info(f"displaying available models to user from {type}.json")
            else:
                logging.info(f"serving {content[choice]} from getmodel()")
                return content[choice]
        except Exception as e:
            print("Please input a valid model. ")
            continue

def view(type):
    model = getmodel(type)
    logging.info(f"displaying model info: \n{model}")
    
    for key, val in model.items():
        print(f"{key}: {val}")
    return 1


def add():
    
    typetoadd = input("input type to add [i(em)/b(luetooth)/d(ac)/q(uit)]: ").strip().lower()
    while typetoadd not in ['i','b','d','q', 'iem', 'bluetooth', 'dac', 'quit']:
        typetoadd = input("input type to add [i(em)/b(luetooth)/d(ac)/q(uit)]: ").strip().lower()
    
    name = getpresentinput("input model name: ")
    
    
    if typetoadd == 'i' or typetoadd == 'iem':
        file = "iem"
        
        freqmax = gettypeinput("Input the maximum frequency: ")
        freqmin = gettypeinput("Input the minimum frequency: ")
        sensbase = gettypeinput("Input the sensitivity: ", "float")
        sensvar = gettypeinput("Input the variance in the sensitivity: ", "float")
        impbase = gettypeinput("Input the impedance: ", "float")
        impvar = gettypeinput("Input the variance in the impedance: ", "float")
        drivers = getpresentinput("Input the drivers in the format 'DD:0,BA:0,PLANAR:0': ")
        price = gettypeinput("Input the price", "float")
        
        cont = Earphone(name, freqmax, freqmin, sensbase, sensvar, impbase, impvar, drivers, price)
        
        filecontent = parsejson(file)
        
        filecontent[name] = cont.todict()
        
        with open("{file}.json", "w+") as f:
            json.dump(filecontent, f, indent=4)
            
        return 1
    
    elif typetoadd == 'b' or typetoadd == 'bluetooth':
        file = "bluetooth"
        
        btver = gettypeinput("Input the bluetooth version: ", "float")
        anc = gettypeinput("Input ANC capability [True/False]: ", "bool")
        maximumdist = gettypeinput("Input maximum distance: ", "int")
        batterylife = gettypeinput("Input total battery life: ", "int")
        earphonebatterycapacity = gettypeinput("Input earphone battery capacity: ", "int")
        casebatterycapacity = gettypeinput("Input case battery capacity: ", "int")
        price = gettypeinput("Input price: ", "int")
        
        cont = Bluetooth(name, btver, anc, maximumdist, batterylife, earphonebatterycapacity, casebatterycapacity)
        
        filecontent = parsejson(file)
        
        filecontent[name] = cont.todict()
        
        with open("{file}.json", "w+") as f:
            json.dump(filecontent, f, indent=4)
            
        return 1
    
    elif typetoadd == 'd' or typetoadd == 'dac':
        file = "dac"
        
        freqmin = gettypeinput("Input minimum frequency: ", "float")
        freqmax = gettypeinput("Input maximum frequency", "float")
        impmin = gettypeinput("Input minimum impedance: ", "float")
        impmax = gettypeinput("Input maximum impedance: ", "float")
        inputport = gettypeinput("Input input port type [2.5/3.5/4.4]: ", "port")
        outputport = gettypeinput("Input output port type [2.5/3.5/4.4]: ")
        amplifierchip = gettypeinput("Input amplifier chip [true/false]: ", "bool")
        decodingchip = gettypeinput("Input decoding chip [true/false]: ", "bool")
        price = gettypeinput("Input price: ")
        
        cont = Dac(name, freqmin, freqmax, impmin, impmax, inputport, outputport, amplifierchip, decodingchip, price)
        
        filecontent = parsejson(file)
        
        filecontent[name] = cont.todict()
        
        with open("{file}.json", "w+") as f:
            json.dump(filecontent, f, indent=4)
        
        return 1
    
    elif typetoadd == 'q' or typetoadd == 'quit':
        return 0