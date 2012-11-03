#!/usr/bin/env python
'''
Created on Sep 28, 2012

@author: josh
'''
#========================CLASS DEFINING EQUIPMENT CREATION===================================s
class Equipment:
    def __init__(self, attack_value, defense_value, name, description, is_armor, buy_value, sell_value):
        self.is_armor=is_armor
        self.name=name
        self.description=description
        self.attack_value=attack_value
        self.defense_value=defense_value
        self.buy_value=buy_value
        self.sell_value=sell_value

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    def to_string(self):
        return self.name.join(self.attack_value)

    def attack(self):
        return str(self.attack_value)
    def defend(self):
        return str(self.defend_value)
