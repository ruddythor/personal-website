'''
Created on Sep 27, 2012

@author: josh
'''
import dice

class Player:
    def __init__(self, Name, level):
        self.level=level
        self.Name=Name
        die=diceRoll.Die()
        self.hpmax=die.roll(15, 6)
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
        hitdice=diceRoller.Die()
        attack = hitdice.roll(attack_value, 6)
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
#            self.equipped_items.append(item)

        if armors<2 and item.is_armor==True:
            self.equipped_items.append(item)
        if weapons<2 and item.is_armor==False:
            self.equipped_items.append(item)

    def unequip(self, item):
        self.equipped_items.remove(item)

    def display_inventory(self):
        print "\nThese are the items in your inventory:\n"
        for item in self.equipment:
            print "\t", item
        return

    def display_equipped(self):
        print "\nThese are your equipped items:\n"
        for item in self.equipped_items:
            print "\t", item, "attack value: ", item.attack_value, "defense value: ", item.defense_value
#            print "\t", item
        return

    def buy(self, item):
        self.equipment.append(item)
        self.gold=self.gold-item.buy_value

    def sell(self, item):
        self.equipment.remove(item)
        self.gold+=item.sell_value
