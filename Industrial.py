from Planet import Planet
class Industrial(Planet):

    def __init__(self):
        super().__init__(self, chipPrice = 25)
        
    def getFighterPrice(self):
        return self.fighterPrice