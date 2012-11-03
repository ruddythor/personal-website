#!/usr/bin/env python
'''
Created on Oct 28, 2012

@author: matthew
'''
#mbrown34 = github account

import player
import random
import menus
import diceRoll
import generator

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
	generator = generator.Generator()
	enemyName, enemyDesc, enemyHP, enemyBaseAttack, enemyBaseDefense, xpVal, renownVal, goldDie = generator.getEnemy()
	print "A", enemyName, " has appeared. "	
	#if playerLevel > enemyLevel
		#print "\nThe", enemyName, "looks kind of weak."
	#elif playerLevel < enemyLevel
		#if enemyLevel-playerLevel > 2
			#print "\nThe", enemyName, "looks pretty tough."
		#else:
			#print "\nThe", enemyNem, "should be a decent challenge."
	#else:
		#print "\nThe 
	die = diceRoll.die()
	playerInit = 0
	enemyInit = 0
	while playerInit == enemyInit	
		playerInit = die.roll(1, 20)
		enemyInit = die.roll(1, 20)
	while endFight != True
		pDamage, eDamage, endFight = batRound(playerInit, enemyInit, playerAttack, playerDefense, enemyAttack, enemyDefense)
		pTotDamage += pDamage
		eTotDamage += eDamage
		if enemyHP-pTotDamage <= 0
			playerWin()
			endFight = True
		elif playerHP-eTotDamage <= 0
			playerLoss()
			endFight = True
		

def batRound(self, playerInit, enemyInit, playerAttack, playerDefense, enemyAttack, enemyDefense):
	battleEnd = False
	if playerInit > enemyInit
	    	pDamage, battleEnd = playerTurn(battleEnd, playerAttack, enemyDefense)
		eDamage = enemyTurn(enemyAttack, playerDefense)
		return battleEnd
	else:
	        eDamage = enemyTurn(enemyAttack, playerDefense)
		pDamage, battleEnd = playerTurn(battleEnd, playerAttack, enemyDefense)
		return battleEnd
	
def playerTurn(self, battleEnd, playerAttack, enemyDefense):
	choice = 0
	while choice < 1 or > 4		
		print "\n\t\tBATTLE MENU\n\t1) Attack\n\t2) Item\n\t3) Magic\n\t4) Surrender"
		choice = input(">>")
		if choice == 1:
			pDamage = playerAttack(playerAttack, enemyDefense)
			return pDamage
		elif choice == 2:
			useItem()
		elif choice == 3:
			useSpell()
		elif choice == 4:
			battleEnd = retreat()
			return battleEnd
		else:
			print "That is not a valid choice. Please re-enter your choice."
	#check enemyHP to see if it remains greater than 0
	#if so, continue battle sequence by returning the battleEnd = False value to calling function and enemy's current HP


def retreat(self, battleEnd):
	choice = 0
	while choice < 1 or choice > 2
	    print "Do you really want to retreat from the battle...\n1) yes\n2) no"
	    choice = input(">>")
	    if choice == 1
		battleEnd = True
		return battleEnd
	    elif choice == 2
		break
	    else:
		"Invalid input."
