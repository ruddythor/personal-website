'''
Created on Sep 27, 2012

@author: josh
'''
#!/usr/bin/env python
import random
import string
import time
import sys
import character
import dice
import equipment

#===========================INSTANTIATES PLAYERONE OF THE PLAYER CLASS AND TESTS SOME OF THE METHODS AND VARIABLES=========================
playerone=character.Player("Charles", 1)
#print playerone.Name
#print "This is the player's max HP"
#print playerone.hpmax
#print "This is the player's base attack value"
#print playerone.base_attack
#print "This is the player's base defense value"
#print playerone.base_defense
#print "This is the player's attack value"
#print playerone.attack()
#print "This is the player's defense value"
#print playerone.defend()

#FUNCTION FOR ACTUAL COMBAT




#======================ESTABLISHING WEAPONS AND ARMOR================================

longsword=equipment.Equipment(10, 0, "long sword", "A bad-ass slayer of women and small men", False, 50, 15)
#print "This is the longsword's attack value"
#print longsword.attack()
shortsword=equipment.Equipment(7, 0, "short sword", "A not-so-bad-ass slayer of women and small men", False, 25, 7)
#print "this is the short sword's attack value"
#print shortsword.attack()

dagger=equipment.Equipment(4, 0, "dagger", "A small dagger, capable of killing someone, but only if you get really cloes to them.", False, 15, 4)
lightarmor=equipment.Equipment(0, 5, "light armor", "A simple piece of armor that barely protects you. It is very simple looking.", True, 65, 20)
heavyarmor=equipment.Equipment(0,15, "heavy armor", "A complex piece of armor that protects you strongly.", True, 100, 25)

global available_items
available_items={1:dagger, 2:shortsword, 3:longsword, 4:lightarmor, 5:heavyarmor}


#===========================================ESTABLISHING SOME ENEMIES==========================




class Enemy:
    def __init__(self, Name, hp_dice, base_attack, base_defense):
        self.Name=Name
        die=dice.Die()
#        print "this is the die roll"
        self.hproll=die.roll(hp_dice, 6)
        self.myrolls=die.myrolls
        self.hpmax=die.total
        self.base_attack=base_attack
        self.base_defense=base_defense
        self.equipment=[]
        self.equipped_items=[]
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
        # if self.equipment.index(item):
        # self.equipped_items.append(item)

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







#===========================================TESTING MORE FUNCTIONS OF THE PLAYER CLASS. THEY ALL SEEM TO WORK==========================
playerone.add(longsword)
playerone.add(shortsword)
playerone.add(lightarmor)
playerone.add(heavyarmor)
playerone.equip(shortsword)
playerone.equip(lightarmor)
#playerone.display_inventory()
#playerone.display_equipped()

#print "NOW, this is the player's attack value, because we equipped a short sword"
#print playerone.attack()
#playerone.unequip(shortsword)
#playerone.equip(longsword)
#playerone.display_equipped()
#print "NOW, this is the player's attack value, because we equipped a Long sword"
#print playerone.attack()
#print playerone.defend()





rat=Enemy("A Rat", 10, 1, 1)
#hitdice=Die()
#hitdice.roll(rat.attack(), 6)
#attack=hitdice.total
#print attack
print 
print
print rat.myrolls
print
print
print rat.attack()
print
print "this is the rat's hp, base attack and base defense"
print rat.hpmax, rat.base_attack, rat.base_defense
print 
print
print "This is the player's HP"
print playerone.hpmax
print "This is a sample of player one's attack roll"
print playerone.attack()
#print playerone.attack()
#print playerone.attack()
#print playerone.attack()







#=========================================NOW FOR THE FUNCTIONS OF THE GAME=============================================






#class MenuClass:
#    def __init__(self):
#        Name="Menu Class"

def main_menu():
    print """



You have the following options:

\t1: Enter the store.
\t2: Enter the arena to fight.
\t3: Display player information.
\t4: Change weapon and armor loadout.
\t5: Quit

                                Enter a number and press enter."""
    player_choice=input("\n>>")
    if player_choice==1:
        store()
    elif player_choice==2:
        arena()
    elif player_choice==3:
        info()
    elif player_choice==4:
        change_equipment()
    elif player_choice==5:
        quit()
    else:
        main_menu()

def store():
    global available_items
    print """





Enter 1 to buy something. Enter 2 to sell something."""
    buy_or_sell=input("\n>>")
    if buy_or_sell==1:
        buy()
    elif buy_or_sell==2:
        sell()

def buy():
    global available_items
    print """




The following items are available for purchase:"""
    for key in available_items:
        print "\t", key, ":", available_items[key], "\t", available_items[key].buy_value, "gold"

    print """You have %i gold.
Enter the number of the item you'd like to purchase.""" %playerone.gold
    purchase_item=input(">>")
    if available_items[purchase_item].buy_value<=playerone.gold:
        playerone.add(available_items[purchase_item])
        playerone.gold=playerone.gold-available_items[purchase_item].buy_value
    print "You now have %i gold" % playerone.gold
    main_menu()

def sell():
    print """




You have the following items to sell:"""
    for x in playerone.equipment:
        print "\t", x, "\t", x.sell_value, "gold"
    print "Enter the number of the item you'd like to sell."
    sell_item=input(">>")





def change_equipment():
    print """




The following items are equippable by you:"""
    print
    for x in playerone.equipment:
        print "\t", x
    print "\nWhat would you like to equip?"
    equip_this=input(">>")



def arena():
    #========================================================THE COMBAT     LOOP=======================================================
    enemy_hp=rat.hpmax
    enemy_defend=rat.defend()
    playerone_hp=playerone.hpmax
    print "Rat's HP"
    print rat.hpmax
    your_defend=playerone.defend()
    enemy_attack=rat.attack()
    your_attack=playerone.attack()
    while enemy_hp or playerone_hp >=0:
        your_attack=your_attack-enemy_defend
        enemy_attack=enemy_attack-your_defend    
        #NEED A CHECK TO KEEP HP PERMANENT
        if enemy_attack>=your_defend:
            playerone_hp=playerone_hp-enemy_attack
        elif your_attack>=enemy_defend:
            enemy_hp=enemy_hp-your_attack
        else:
            enemy_attack=rat.attack()
        print enemy_attack
        print "This is the enemy's hp", enemy_hp
        print "This is your hp", playerone_hp

        if enemy_hp<=0:
            print "You defeated the enemy"
            print "enemy's hp", enemy_hp
            print "Your hp", playerone_hp
            main_menu()
            break
        #will need a function to divvy out rewards if you win
        elif playerone_hp<=0:
            print "You died"
            print "enemy's hp", enemy_hp
            print "Your hp", playerone_hp
            break

def info():
	print """This is your character's information: #@IndentOk
	\tplayerone.level
	\tplayerone.Name
	\tplayerone.hpmax
	\tplayerone.base_attack
	\tplayerone.base_defense
	\tplayerone.gold"""

#		self.equipment=[]
#		self.equipped_items=[]




def quit():
    sys.exit()


#main_menu()



#arena()


        



