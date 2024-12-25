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
    
    def todict(self):
        return {
            "name": self.name,
            "maximum frequency": self.freqmax,
            "minimum frequency": self.freqmin,
            "base sensitivity": self.sensbase,
            "sensitivity variability": self.sensvar,
            "base impedance": self.impbase,
            "impedance variability": self.impvar,
            "drivers": self.drivers,
            "price": self.price
        }
    
    @staticmethod
    def fromdict(data):
        return Earphone(
            name=data["name"],
            freqmax=data["maximum frequency"],
            freqmin=data["minimum frequency"],
            sensbase=data["base sensitivity"],
            sensvar=data["sensitivity variability"],
            impbase=data["base impedance"],
            impvar=data["impedance variability"],
            drivers=data["drivers"],
            price=data["price"]
        )

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
    
    def todict(self):
        return {
            "name": self.name,
            "bluetooth version": self.btver,
            "anc": self.anc,
            "prot": self.prot,
            "maximum distance": self.maxdist,
            "battery life": self.battlife,
            "earphone battery capacity": self.earbattcap,
            "case battery capacity": self.casebattcap,
            "price": self.price
        }
        
    @staticmethod
    def fromdict(data):
        return Bluetooth(
            name=data["name"],
            bluetoothversion=data["bluetooth version"],
            anc=data["anc"],
            prot=data["prot"],
            maximumdistance=data["maximum distance"],
            batterylife=data["battery life"],
            earphonebatterycapacity=data["earphone battery capacity"],
            casebatterycapacity=data["case battery capacity"],
            price=data["price"]
        )
                
class Dac:
    def __init__(self, name: str, snr: int, dnr: int, thdn: int, minimumfrequency: int, maximumfrequency: int, minimumimpedance: int, maximumimpedance: int, inputport: str, outputport: str, amplifierchip: bool, decodingchip: bool, price: float):
        self.name = name
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
        
    def todict(self):
        return {
            "name": self.name,
            "snr": self.snr,
            "dnr": self.dnr,
            "thdn": self.thdn,
            "minimum frequency": self.freqmin,
            "maximum frequency": self.freqmax,
            "minimum impedance": self.impmin,
            "maximum impedance": self.impmax,
            "input port": self.inputport,
            "output port": self.outputport,
            "amplifier chip": self.amplifierchip,
            "decoding chip": self.decodingchip,
            "price": self.price
        }
    
    @staticmethod
    def fromdict(data):
        return Dac(
            name=data["name"],
            snr=data["snr"],
            dnr=data["dnr"],
            thdn=data["thdn"],
            minimumfrequency=data["minimum frequency"],
            maximumfrequency=data["maximum frequency"],
            minimumimpedance=data["minimum impedance"],
            maximumimpedance=data["maximum impedance"],
            inputport=data["input port"],
            outputport=data["output port"],
            amplifierchip=data["amplifier chip"],
            decodingchip=data["decoding chip"],
            price=data["price"]
        )
        