'''
Created October 28, 2012


@author matthew
'''

import DiceRoller
import sys
import enemyGen
import foelist

gameExit = False

while gameExit != True:
	
	generator = enemyGen.Generator()
	
	name, hp, baseAttack, baseDefense, xpVal, renownVal, goldDie = generator.getEnemy()
	print "", name, " was generated with ", hp, " HP."
	print "\nThe enemy's other stats are:\n"
	print "\tBase Attack: ", baseAttack, "\n\tBase Defense: ", baseDefense
	print "\n\tXP Value: ", xpVal, "\n\tRenown Value: ", renownVal
	print "\n\tGold Drop Value: ", goldDie		
	choice = 0    	
	while choice < 1 or choice > 2:	
		print "Continue? (1 = yes/2 = no)"
		choice = input("\n>>")
		if choice == 1:
			gameExit = False
		elif choice == 2:
			gameExit = True
		else:
			print "I did not catch that..."
	
sys.exit()
		
