'''
Created October 28, 2012

@author matthew
'''
import diceRoll
import random

class Generator:	      
	def __init__(self):
		pass
 	def __str__(self):
		return 'Generator'
	def __repr__(self):
		return 'Generator'

	def setHealth(self, hp_dice):
		die = diceRoll.Die()
		hp = die.roll(hp_dice, 6)
		return hp

	def setGold(self, gold):
		die = diceRoll.Die()
		goldAmt = die.roll(gold, 6)
		return goldAmt

	def getEnemy(self):
		generator = Generator()
		badguy = []
		from enemylist import enemylist
		enemy = random.choice(enemylist)
		badguy = enemy[:]
		hp = generator.setHealth(enemy[2])
		goldDrop = generator.setGold(enemy[7])
		badguy[2] = hp
		badguy[7] = goldDrop
		return badguy

class Character:	      
	def __init__(self):
		pass
 	def __str__(self):
		return 'Character'
	def __repr__(self):
		return 'Character'

	def getName(self):
		name = input("Enter the character's name: \n>>")
		return name
	
	#def loadChar(self):
		#this will be a function to load a previously saved character

	#def saveChar(self):
		#this will be a function to save a character's stats and inventory

	def genChar(self):
		character = Character()
		generator = Generator()
		name = character.getName
		level = 1
		health = generator.setHealth(15)
		baseAttack = 3
		baseDefense = 2
		inventory = []
		equip = []
		gold = 50
		xp = 0
		renown = 0
		return name, level, health, baseAttack, baseDefense, inventory, equip, gold, xp, renown
