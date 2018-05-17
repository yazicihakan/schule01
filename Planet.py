class Planet():
    
    def __init__(self, fighterPrice = 125, cargoPrice = 100, curryPrice = 50, chipPrice = 50, weaponPrice = 50):
        self.fighterPrice = fighterPrice
        self.cargoPrice = cargoPrice
        self.curryPrice = curryPrice
        self.chipPrice = chipPrice
        self.weaponPrice = weaponPrice

    def getCargoPrice(self):
        return self.cargoPrice
    def getCurryPrice(self):
        return self.curryPrice
    def getChipPrice(self):
        return self.chipPrice
    def getWeaponPrice(self):
        return self.weaponPrice