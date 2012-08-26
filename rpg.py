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
#		for x in self.myrolls:
#			self.myrolls.remove(x)
		for x in range(1, dice+1):
			self.myrolls.append(random.randrange(1, sides))
		for x in self.myrolls:
			print x,
		return


class Player:
	def __init__(self):
		Name = ""
		die=Die()
		self.hproll=die.roll(4, 6)
		self.hpmax=0
		for x in self.hproll:
			self.hpmax += x
		print self.hpmax
		self.base_attack=5
		self.base_defense=3
		self.equipment=[]
		self.equipped_items=[]


	def attack(self):
		attack_value=self.base_attack
		for item in self.equipped_items:
			attack_value+=item.attack

	def defend(self):
		defense_value=self.base_defense
		for item in self.equipped_items:
			defense_value+=item.defense

	def add(self, item):
		self.equipment.append(item)

	def drop(self, weapon):
		self.equipment.remove(item)

	def equip(self, item):
		if self.equipment.index(item):
			self.equipped_items.append(item)


playerone=Player()
print playerone.hp
print playerone.base_attack
print playerone.base_defense
playerone.attack()#THIS WILL RETURN ATTACK VALUE 
playerone.defend()#RETURNS DEFENSE VALUE

#FUNCTION FOR ACTUAL COMBAT


class Equipment:
	def __init__(self, attack_value, defense_value, name, description):
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

longsword=Equipment(10, 0, "Long sword", "A bad-ass slayer of women and small men")
print longsword.attack()
shortsword=Equipment(7, 0, "short sword", "A not-so-bad-ass slayer of women and small men")





gold=100
strength=10
healthmax=15
hp=healthmax
movement=5
charlevel=1
defense=0
roll=Die()
attack=0

inventory=[]
weapons=[shortsword, longsword]
armor=[]
goal= 0


def actionfunc():
	global goal
	action=raw_input("\n\nWhat would you like to do? ['fight', 'move', 'drop item', 'pick up', 'equip [weapon, armor]', 'unequip [weapon, armor]', 'info', 'rest', 'quit']\n>>")
	if action == "equip weapon":
		equipweaponfunc()
		goal += 1
	elif action == "unequip weapon":
		unequipweaponfunc()
		goal = goal + 1

	elif action == "equip armor":
		equiparmorfunc()
		goal+=1
	elif action == "unequip armor":
		unequiparmorfunc()
		goal = goal + 1
	elif action == "fight":
		fight()
		goal = goal + 1
	elif action == "quit":
		quit()
		goal = goal + 1
	elif action == "drop item":
		dropitem()
		goal = goal + 1
	elif action == "move":
		move()
		goal = goal + 1
	elif action == "pickup item":
		pickup()
		goal = goal + 1
	elif action == "rest":
		goal = goal + 1
		rest()
	elif action == "info":
		info()

	else:
		print "Invalid instruction. Please try again."
		actionfunc()


def rest():
	global hp
	global healthmax
	hp=healthmax

def quit():
	global goal
	goal=5



def info():
	global healthmax, hp, inventory, weapons, armor, gold, strength, movement, charlevel, equippedarmor, equippedweapon, defense, attack

	print "your character is level", charlevel
	print "Your current health is ", hp, "out of", healthmax
	print "You have", gold, "gold pieces."
	print "Your inventory consists of:"
	for x in inventory:
		print "\t", x
	for x in weapons:
		print "\t", x
	for x in armor:
		print "\t", x
	print "Your strength is", strength
	print "Your movement value is", movement
	print "your defense value is", defense
	print "Your attack value is", attack
	print "you have equipped,", equippedweapon, equippedarmor




#while goal <=5:
#	actionfunc()
