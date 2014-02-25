'''
Created on Oct 1, 2012

@author: josh
'''
from dice import Die
from django.db import models


class Enemy(models.Model):
    name = models.TextField(default="An Enemy!")
    xp_value = models.IntegerField(default=5)
    renown_value = models.IntegerField(default=10)
    hpmax = models.IntegerField()
    current_hp = models.IntegerField(default=0)
    base_attack = models.IntegerField(default=4)
    base_defense = models.IntegerField(default=5)
    gold = models.IntegerField()

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    class Meta:
        app_label = 'arenafighter'

    def __init__(self, *args, **kwargs):
        super(Enemy, self).__init__(*args, **kwargs)
        die = Die()
        self.hpmax = die.roll(15, 6)
        self.current_hp = self.hpmax
        self.gold = die.roll(5, 6)

    def attack(self):
        attack_value=self.base_attack
#        for item in self.equipped_items:
#            attack_value+=item.attack_value
        dice = Die()
        attack = dice.roll(attack_value, 6)
        return attack

    def defense_value(self):
        defense_value=self.base_defense
#        for item in self.equipped_items:
#            defense_value+=item.defense_value
        return defense_value

    def add(self, item):
        self.equipment.append(item)

    def drop(self, item):
        self.equipment.remove(item)

    def equip(self, item):
        pass
#        weapons=0
#        armors=0
#        for x in self.equipped_items:
#            if x.is_armor==True:
#                armors+=1
#            else:
#                weapons+=1
#        if len(self.equipped_items)>2:
#            self.equipped_items.pop(0)#

#        if self.equipment.index(item):
#            if armors<=0 and item.is_armor==True:
#                self.equipped_items.append(item)
#            elif weapons<=1 and item.is_armor==False:
#                self.equipped_items.append(item)
#        else:
#            print "You have too many of that type of item equipped. Try again."#

    def unequip(self, item):
#        self.equipped_items.remove(item)
        pass

    def display_inventory(self):
#        for item in self.equipment:
#            print "\t", item
#        return
        pass

    def display_equipped(self):
        pass
#        print "These are your equipped items"
#        for item in self.equipped_items:
#            print "\t", item
#        return

