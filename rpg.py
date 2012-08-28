#!/usr/bin/env python
import random
import string

class Die:
	def __init__(self):
		myclass='this is the die roll class'
		self.myrolls=[]
	def __str__(self):
		return 'Dieroll'
	def __repr__(self):
		return 'Dieroll'
#	@staticmethod
	def roll(self, dice, sides):
		for x in self.myrolls:
			self.myrolls.remove(x)
		self.total=0
		for x in range(1, dice+1):
			self.myrolls.append(random.randrange(1, sides))
		for x in self.myrolls:
			self.total+=x
			print x,
#		print "This is the total for the die roll"
#		print self.total
		return


#======================================CREATES THE PLAYER CLASS WITH <ATTACK> <DEFEND> <ADD> <DROP> <EQUIP> <UNEQUIP> <DISPLAY_INVENTORY> AND <DISPLAY_EQUIPPED> METHODS=========================================================
class Player:
	def __init__(self, Name):
		self.Name=Name
		die=Die()
		print "this is the die roll"
		self.hproll=die.roll(15, 6)
		self.hpmax=die.total
		self.base_attack=3
		self.base_defense=2
		self.equipment=[]
		self.equipped_items=[]

	def attack(self):
		attack_value=self.base_attack
		for item in self.equipped_items:
			attack_value+=item.attack_value
		return attack_value

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
		if len(self.equipped_items)>2:
			self.equipped_items.pop(0)
		weapons=0
		armors=0
		for x in self.equipped_items:
			if x.is_armor==True:
				armors+=1
			else:
				weapons+=1
		if armors<=0 and item.is_armor==True:
			self.equipped_items.append(item)
		elif weapons<=1 and item.is_armor==False:
			self.equipped_items.append(item)
		else:
			print "You have too many of that type of item equipped. Try again."
		# if self.equipment.index(item):
		# self.equipped_items.append(item

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
#===========================INSTANTIATES PLAYERONE OF THE PLAYER CLASS AND TESTS SOME OF THE METHODS AND VARIABLES=========================
playerone=Player("Charles")
print playerone.Name
print "This is the player's max HP"
print playerone.hpmax
print "This is the player's base attack value"
print playerone.base_attack
print "This is the player's base defense value"
print playerone.base_defense
print "This is the player's attack value"
print playerone.attack()
print "This is the player's defense value"
print playerone.defend()

#FUNCTION FOR ACTUAL COMBAT

#========================CLASS DEFINING EQUIPMENT CREATION===================================s
class Equipment:
	def __init__(self, attack_value, defense_value, name, description, is_armor):
		self.is_armor=is_armor
		self.name=name
		self.description=description
		self.attack_value=attack_value
		self.defense_value=defense_value

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


#======================ESTABLISHING WEAPONS AND ARMOR================================

longsword=Equipment(10, 0, "long sword", "A bad-ass slayer of women and small men", False)
print "This is the longsword's attack value"
print longsword.attack()
shortsword=Equipment(7, 0, "short sword", "A not-so-bad-ass slayer of women and small men", False)
print "this is the short sword's attack value"
print shortsword.attack()

lightarmor=Equipment(0, 5, "light armor", "A simple piece of armor that barely protects you. It is very simple looking.", True)

heavyarmor=Equipment(0,15, "heavy armor", "A complex piece of armor that protects you strongly.", True)








#===========================================TESTING MORE FUNCTIONS OF THE PLAYER CLASS. THEY ALL SEEM TO WORK==========================
playerone.add(longsword)
playerone.add(shortsword)
playerone.add(lightarmor)
playerone.add(heavyarmor)
playerone.equip(shortsword)
playerone.equip(lightarmor)
playerone.display_inventory()
playerone.display_equipped()

print "NOW, this is the player's attack value, because we equipped a short sword"
print playerone.attack()
playerone.unequip(shortsword)
playerone.equip(longsword)
playerone.display_equipped()
print "NOW, this is the player's attack value, because we equipped a Long sword"
print playerone.attack()
print playerone.defend()


playerone.equip(heavyarmor)
playerone.display_equipped()
print
print
playerone.equip(shortsword)
playerone.add(longsword)
playerone.equip(longsword)
print playerone.equipped_items
print len(playerone.equipped_items)
print playerone.attack()
playerone.equip(heavyarmor)
print playerone.equipped_items
playerone.equip(longsword)
playerone.equip(longsword)
playerone.equip(shortsword)
print playerone.equipped_items
playerone.equip(heavyarmor)
print playerone.equipped_items
print playerone.attack()
print playerone.defend()
print "that was the defense value. number above is attack"
