#!/usr/bin/env python
'''
Created on Oct 28, 2012

@author: matthew
'''
#changed enemylist from the need to create a list variable and then add that list variable to the enemylist []
#now the person adding a new enemy can simply add another list into the main list by using the syntax below
#syntax for creating a new enemy type ==
	                                      #[   1,        2,            3,          4,          5,         6,           7,          8   ] 
#user entered string to create new enemy == ", ["Name", "description", hp_dice, base_attack, base_defense, xp_value, renown_value, gold_die]"
            #begin list of foes
	    #", [    1,                 2,           3,  4, 5,  6, 7, 8]"
	    #", ['barbarian', "A brutish barbarian", 15, 8, 5, 15, 5, 5]"
enemylist = [   ['barbarian', "A brutish barbarian", 15, 8, 5, 15, 5, 5], ['rat', "A fairly weak rat", 10, 3, 1, 5, 2, 2], 
                ['soldier', "A well-trained soldier", 17, 9, 7, 17, 8, 10] 
	    ]#end of list of foes

		
