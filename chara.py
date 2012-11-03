"""
Created on November 2, 2012


@author matthew
"""
import diceRoll

class Player:
    def __init__(self):
        pass
    def __str__(self):
        return 'Player'
    def __repr__(self):
	return 'Player'

def newChar(self):
	char=chara.Player()
	die=diceRoll.Die()
	hp = die.roll(15,6)
	print "What will the new character's name be?"
	Name = input("\n>>")
	baseAttack=3
	baseDefense=2
	gold=50
	xp=0
	renown=0
	charItems=[]
	charEquip=[]
	char=[Name, hp, baseAttack, baseDefense, gold, xp, renown]
	charStats=['STR','DEX','CON','INT','WIS','CHA']
	charStatVals=['STR']
	x=0
	while x < 6:
		charStatVals.append(die.roll(3,6)
		x+=1
	charStatVals = char.increaseStats(charStatVals)
	char.addItem(healthPotion) #standard starting item
	char.addItem(manaPotion) #standard starting item
	char.addEquip(longsword) #standard starting weapon
	char.addEquip(lightarmor) #standard starting armor
	return char, charStats, charStatVals, charItems, charEquip

def saveChar(self, char, charStats, charStatVals, charItems, charEquip):
	#save file comprising of char, charStats, charStatVals, charItems, charEquip
	pass

def loadChar(self):
	#read file to populate the list fields below which comprise an entire characters stats and eqiupment
	return char, charStats, charStatVals, charItems, charEquip

def increaseStats(self, charStats, charStatVals):
	choice = 0
	die=diceRoll.Die()
	extraPoints=die.roll(3,6)
	while choice <1 or choice >6 and extraPoints > 0
		print "These are your current stat values:\n"
		for x in charStats and charStatVals
			print "\t", charStats[x], "\t", charStatVals[x], "\n"
		print "\nYou have",extraPoints, "to spend on stat increases.\n\tWhich stat would you like to increase?\n\t(You cannot increase a stat of 18\n"
		choice = input(">>")
		if choice == 1 and charStatVals[0] < 18:
			charStatVals[0]+=1
			extraPoints-=1
		elif choice == 2 and charStatVals[1] < 18:
			charStatVals[1]+=1
			extraPoints-=1
		elif choice ==3 and charStatVals[2] < 18:
			charStatVals[2]+=1
			extraPoints-=1
		elif choice ==4 and charStatVals[3] < 18:
			charStatVals[3]+=1
			extraPoints-=1
		elif choice ==5 and charStatVals[4] < 18:
			charStatVals[4]+=1
			extraPoints-=1
		elif choice ==6 and charStatVals[5] < 18:
			charStatVals[5]+=1
			extraPoints-=1
		else:
			print "\nSorry, that stat is maxed out, or the value entered is not recognized.\n\t Please try again"
	print "So, here are the final values for your stats:\n"
		for x in charStats and charStatVals
			print "\n\t", charStats[x], "\t", charStatVals[x]
	input("\n\n...Press enter to continue...")
	return charStatVals

	def addItem(self, )
"""
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
"""
