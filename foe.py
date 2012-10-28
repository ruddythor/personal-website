'''
Created on Oct 1, 2012

@author: josh
'''
import random

class Enemy:
    def __init__(self, Name, hp_dice, base_attack, base_defense, xp_value, renown_value):
        self.Name=Name
        die=dice.Die()
        self.xp_value=xp_value
        self.renown_value=renown_value
        self.hproll=die.roll(hp_dice, 6)
        self.myrolls=die.myrolls
        self.hpmax=die.total
        self.base_attack=base_attack
        self.base_defense=base_defense
        self.equipment=[]
        self.equipped_items=[]
        self.goldroll=die.roll(5, 6)
        self.gold=die.total
#        self.right_hand=[]
#        self.left_hand=[]
#        self.head=[]
    def __str__(self):
        return self.Name
    def __repr__(self):
        return self.Name




