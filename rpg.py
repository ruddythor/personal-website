#!/usr/bin/env python
'''
Created on Sep 27, 2012

@author: josh
'''

import menus
import sys

game_over = False
#simple loop to control the game operation
#game runs until the user selects to quit the game from the menus.main() module
while game_over != True:
	game_over = menus.main()


sys.exit()
