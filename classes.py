class JackSize:
    VALID_STATES = {"2.5", "3.5", "4.4"}

    def __init__(self, state):
        if state not in self.VALID_STATES:
            raise ValueError(f"Invalid state: {state}. Valid states are {', '.join(self.VALID_STATES)}.")
        self.state = state


class Earphone:
    def __init__(self, name: str, freqmax: int, freqmin: int, sensbase: float, sensvar: float, impbase: float, impvar: float, drivers: dict, price: float):
        self.name = name
        self.freqmax = freqmax
        self.freqmin = freqmin
        self.sensbase = sensbase
        self.sensvar = sensvar
        self.impbase = impbase
        self.impvar = impvar
        self.drivers = drivers
        self.price = price

class Bluetooth:
    def __init__(self, name: str, bluetoothversion: float, anc: bool, prot: list, maximumdistance: int, batterylife: int, earphonebatterycapacity: int, casebatterycapacity: int, price: float):
        self.name = name
        self.btver = bluetoothversion
        self.anc = anc
        self.prot = prot
        self.maxdist = maximumdistance
        self.battlife = batterylife
        self.earbattcap = earphonebatterycapacity
        self.casebattcap = casebatterycapacity
        self.price = price
        
class Dac:
    def __init__(self, snr: int, dnr: int, thdn: int, minimumfrequency: int, maximumfrequency: int, minimumimpedance: int, maximumimpedance: int, inputport: str, outputport: str, amplifierchip: bool, decodingchip: bool, price: float):
        self.snr = snr
        self.dnr = dnr
        self.thdn = thdn
        self.freqmin = minimumfrequency
        self.freqmax = maximumfrequency
        self.impmin = minimumimpedance
        self.impmax = maximumimpedance
        self.inputport = inputport
        self.outputport = outputport
        self.amplifierchip = amplifierchip
        self.decodingchip = decodingchip
        self.price = price
        
        
        