#!/usr/bin/env python
import random
import string

class Dieroll:
	def __init__(self):
		myclass='this is the die roll class'
		self.myrolls=[]
	def __str__(self):
			return 'Dieroll'
	def __repr__(self):
		return 'Dieroll'

	def roll(self, dice, sides):
#		for x in self.myrolls:
#			self.myrolls.remove(x)
		for x in range(1, dice+1):
			self.myrolls.append(random.randrange(1, sides))
		for x in self.myrolls:
			print x,
		return


class Inventory:
	def __init__(self):
		Name="Inventory"
	
	def __str__(self):
			return 'Inventory'
	def __repr__(self):
		return 'Inventory'

	def drop(self, item):
		inventory.remove(item)
		weapons.remove(item)

	def pickup(self, item):
		inventory.append(item)

	def use(self, item):
		inventory.remove(item)
		
	def equiparmor(self, item):
		equippedarmor=item

	def equipweapon(self, item):
		equippedweapon=item

	def unequiparmor(self, item):
		equippedarmor="You have no armor equipped."

	def unequipweapon(self, item):
		equippedweapon="You have no weapon equipped."



class Lightarmor:
	def __init__(self):
		Name="A set of light, leathor armor."
		defense=7
	def __str__(self):
			return 'light armor'
	def __repr__(self):
		return 'light armor'
		
	def describe(self):
		return Name

	def equiplightarmor(self):
		equippedarmor=Lightarmor()
		
	def unequiplightarmor(self):
		equippedarmor="You have no armor equipped."


class Clothes:
	def __init__(self):
		Name="A set of clothes."
		defense=3
	def __str__(self):
		return 'clothes'
	def __repr__(self):
		return 'clothes'
		
	def describe(self):
		return Name

	def equipclothes(self):
		equippedarmor=Clothes()
		
	def unequipclothes(self):
		equippedarmor="You have no armor equipped."



class Healthpotion:
	def __init__(self):
		Name="A potion that restores health."
		hprestore=50
	def __str__(self):
			return 'health potion'
	def __repr__(self):
		return 'health potion'
		
	def describe(self):
		return Name





class Shortsword:
	def __init__(self):
		Name="A basic short sword."
		attack=7
		defense=2
	def __str__(self):
			return 'short sword'
	def __repr__(self):
		return 'short sword'


	def describe(self):
		return Name

class Longsword:
	def __init__(self):
		Name="A basic long sword."
		attack=10
		defense=3
	def __str__(self):
			return 'long sword'
	def __repr__(self):
		return 'long sword'
	def describe(self):
		return Name


shortsword=Shortsword()
longsword=Longsword()
lightarmor=Lightarmor()
clothes=Clothes()
healthpotion=Healthpotion()

gold=100
strength=10
healthmax=15
hp=healthmax
movement=5
charlevel=1
defense=0
roll=Dieroll()
attack=0

inventory=[healthpotion]
weapons=[shortsword, longsword]
armor=[lightarmor, clothes]
equippedweapon=shortsword
equippedarmor=clothes
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

def equipweaponfunc():
	global equippedweapon
	print "\nThese are your equippable weapons:"
	for x in weapons:
		print x
	print "\nThis is your equipped weapon:"
	print equippedweapon
	equippedweapon=raw_input("\nWhat would you like to equip?\n>>")
	if equippedweapon == "long sword":
		equippedweapon=Longsword()
	elif equippedweapon == "short sword":
		equippedweapon=Shortsword()
	else:
		print "You did not choose a valid item."
		equippedweapon=raw_input("\nWhat would you like to equip?\n>>")
	print "\nYou have now equipped your", equippedweapon
	print type(equippedweapon)

def rest():
	global hp
	global healthmax
	hp=healthmax

def quit():
	global goal
	goal=5

def equiparmorfunc():
	global equippedarmor
	global lightarmor
	global clothes
	print "\nYou have the following armor to equip:", armor
	print "\nYou currently have equipped:", equippedarmor
	equip=raw_input("\nWhat would you like to equip?\n>>")
	if equip=="clothes":
		equippedarmor=clothes
	elif equip=="light armor":
		equippedarmor=lightarmor
	else:
		print "You did not choose a valid option."
		actionfunc()
	print "\nYou have the following equipped", equippedarmor
	print type(equippedarmor)


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




while goal <=5:
	actionfunc()
