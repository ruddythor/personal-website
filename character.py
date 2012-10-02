'''
Created on Sep 27, 2012

@author: josh
'''
import dice
#======================================CREATES THE PLAYER CLASS WITH <ATTACK> <DEFEND> <ADD> <DROP> <EQUIP> <UNEQUIP> <DISPLAY_INVENTORY> AND <DISPLAY_EQUIPPED> METHODS=========================================================
class Player:
    def __init__(self, Name, level):
        self.level=level
        self.Name=Name
        die=dice.Die()
        self.hproll=die.roll(15, 6)
        self.hpmax=die.total
        self.base_attack=3
        self.base_defense=2
        self.equipment=[]
        self.equipped_items=[]
        self.gold=50
        self.xp=0
        self.renown=0
#        self.right_hand=[]
#        self.left_hand=[]
#        self.head=[]

    def attack(self):
        attack_value=self.base_attack
        for item in self.equipped_items:
            attack_value+=item.attack_value
#        return attack_value
        hitdice=dice.Die()
        hitdice.roll(attack_value, 6)
        attack=hitdice.total
        return attack

    def defend(self):
        defense_value=self.base_defense
        for item in self.equipped_items:
            defense_value+=item.defense_value
        return defense_value

    def add(self, item):
        self.equipment.append(item)

    def drop(self, item):
        self.equipment.remove(item)

    def equip(self, item):

        weapons=0
        armors=0
        for x in self.equipped_items:
            if x.is_armor==True:
                armors+=1
            else:
                weapons+=1

        if len(self.equipped_items)>2:
            self.equipped_items.pop(0)

        if self.equipment.index(item):
            if armors<=0 and item.is_armor==True:
                self.equipped_items.append(item)
            elif weapons<=1 and item.is_armor==False:
                self.equipped_items.append(item)
        else:
            print "You have too many of that type of item equipped. Try again."


    def unequip(self, item):
        self.equipped_items.remove(item)

    def display_inventory(self):
        for item in self.equipment:
            print "\t", item
        return

    def display_equipped(self):
        print "These are your equipped items"
        for item in self.equipped_items:
            print "\t", item
        return

    def buy(self, item):
        self.equipment.append(item)
        self.gold=self.gold-item.buy_value

    def sell(self, item):
        self.equipment.remove(item)
        self.gold+=item.sell_value