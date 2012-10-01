'''
Created on Sep 27, 2012

@author: josh
'''
import random
class Die:
    def __init__(self):
        self.myrolls=[]
    def __str__(self):
        return 'Dieroll'
    def __repr__(self):
        return 'Dieroll'

    def roll(self, dice, sides):
        for x in self.myrolls:
            self.myrolls.remove(x)
        self.total=0
        for x in range(1, dice+1):
            self.myrolls.append(random.randrange(1, sides))
        for x in self.myrolls:
            self.total+=x
        return
