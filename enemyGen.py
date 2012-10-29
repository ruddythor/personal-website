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

	def setHealth(self, hp_dice):
		die = DiceRoller.Die()
		hp = die.roll(hp_dice, 6)
		return hp

	def setGold(self, gold):
		die = DiceRoller.Die()
		goldAmt = die.roll(gold, 6)
		return goldAmt

	def getEnemy(self):
		generator = Generator()
		from foelist import foelist
		enemy = random.choice(foelist)
		Name = enemy[0]
		hp = generator.setHealth(enemy[1])
		baseAttack = enemy[2]
		baseDefense = enemy[3]
		xpVal = enemy[4]
		renownVal = enemy[5]
		goldDie = generator.setGold(enemy[6])
		return Name, hp, baseAttack, baseDefense, xpVal, renownVal, goldDie
