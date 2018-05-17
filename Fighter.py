'''
Created on 04.05.2018

@author: panjeet
'''

from Ship import Ship;

class Fighter(Ship):
    
    def __init__(self, price = 125):
        super().__init__()
        self.price = price

    def getPrice(self):
        return self.price