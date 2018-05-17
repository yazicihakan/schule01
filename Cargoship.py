'''
Created on 04.05.2018

@author: panjeet
'''

from Ship import Ship;

class Cargoship(Ship):

    def __init__(self, cargospace = 10, price = 100):
        super().__init__()
        self.cargospace = cargospace
        self.price = price

    def getCargospace(self):
        return self.cargospace