'''
Created on 04.05.2018

@author: panjeet
'''

class Ship:
    
    shipCount = 0;
    
    def __init__(self):
        self.shipCount += 1
        
    def getPrice(self):
        return self.price