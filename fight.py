#!/usr/bin/env python
'''
Created on Oct 28, 2012

@author: matthew
'''
#mbrown34 = github account

import player
import random
import menus
import DiceRoller
import enemyGen

#display battle menu... i.e. attack, item, magic, surrender
#attack option runs the round() module
	#round() module handles individual attack round 
	#checking attack values to see if a hit is made
	#then dealing damage appropriately for both enemy and player
#item pulls up the battleitem() module which handles equipment that can be used during a fight
	#battleitem() displays the players usable items
	#user then selects which item to use
	#module then uses the item appropriately
	#potions to restore health or magic
	#or attack/status-changing items
#magic option loads a list of the players magical spells
	#spells() module will display the users spells
	#and when one is selected will perform an appropriate action
	#according to the def of the spell
#surrender option will abandon the battle and exit to the menus.main() module
def battle(self):
	endFight = False
	generator = enemyGen.Generator()
	enemyName,  =generator.getEnemy()
	while endFight != True
		batRound()
	

#while endFight != True
#	battle ---- call the round function
#round() establishes initiative and calls playerTurn() or enemyTurn() appropriately
#after functions are performed, a check decides if the
#
#

def batRound(self):
	die = DiceRoller.die()
	playerInit, enemyInit
	playerAttack, enemyAttack, playerDamage, enemyDamage
	
	'''
	
	LOGIC for battle round
	--while playerInitiative == enemyInitiative -> get random rolls for initiative for player and enemy
	----compare initiative rolls to see who is higher
	 if playerInitiative > enemyInitiative
	------playerRound(check playerAttack to see if attack is landed, return playerDamage)
	------enemyRound(check enemyAttack to see if attack is landed, return enemyDamage)
	 else
	------enemyRound(same as above)
	------playerRound(same as above)
	
	'''
	


