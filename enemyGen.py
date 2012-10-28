'''
Created October 28, 2012


@author matthew
'''

import DiceRoller
import random


class Generator:	      
	def __init__(self):
		pass
        	
	def __str__(self):
		return 'Generator'
	def __repr__(self):
		return 'Generator'
	
	
	def setName(self, name):
		Name = name
		return Name

	def setHealth(self, hp_dice):
		die = DiceRoller.Die()
		hp = die.roll(hp_dice, 6)
		return hp

	def setGold(self, gold):
		die = DiceRoller.Die()
		goldAmt = die.roll(gold, 6)
		return goldAmt

	def setAttack(self, attackVal):
		attack = attackVal
		return attack

	def getEnemy(self):
		generator = Generator()
		from foelist import foelist
		enemy = random.choice(foelist)
		Name = generator.setName(enemy[0])
		hp = generator.setHealth(enemy[1])
		return Name, hp
