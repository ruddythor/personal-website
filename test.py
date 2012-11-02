'''
Created October 28, 2012


@author matthew
'''

import diceRoll
import sys
import generator
import enemylist
import foe

gameExit = False

while gameExit != True:
	
	gen = generator.Generator()
	enemy = gen.getEnemy()
	print "A", enemy[0], "(", enemy[1], ") was generated with", enemy[2], "HP."
	print "\nThe enemy's other stats are:"
	print "\tBase Attack: ", enemy[3], "\n\tBase Defense: ", enemy[4]
	print "\tXP Value: ", enemy[5], "\n\tRenown Value: ", enemy[6]
	print "\tGold Drop Value: ", enemy[7]		
	choice = 0    	
	while choice < 1 or choice > 2:	
		print "Continue?\n1 = yes  2 = no"
		choice = input("\n>>")
		if choice == 1:
			gameExit = False
		elif choice == 2:
			gameExit = True
		else:
			print "I did not catch that..."
	
sys.exit()
		
