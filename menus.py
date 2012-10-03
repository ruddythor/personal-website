#!/usr/bin/env python
'''
Created on Oct 3, 2012

@author: josh
'''
import player
def main():
    print """\n\n\n\n
    You have the following options:
    \t1: Enter the store.
    \t2: Enter the arena to fight.
    \t3: Display player information.
    \t4: Change weapon and armor loadout.
    \t5: Quit
                             Enter a number and press enter."""
    player_choice=input("\n>>")
    if player_choice==1:
        import store
        store.main()
    elif player_choice==2:
        import arena
        arena.fight()
    elif player_choice==3:
        info()
    elif player_choice==4:
        change_equipment()
    elif player_choice==5:
        quit()
#    else:
#        main()
 
def change_equipment():
    print """\n\n\n\n\nThe following items are equippable by you:"""
    print
    for x in player.playerone.equipment:
        print "\t", x
    print "\nWhat would you like to equip?"
    equip_this=input(">>")

def info():
    print """This is your character's information:
    \tplayer.playerone.level
    \tplayer.playerone.Name
    \tplayer.playerone.hpmax
    \tplayer.playerone.base_attack
    \tplayer.playerone.base_defense
    \tplayer.playerone.gold"""
    main()
#        self.equipment=[]
#        self.equipped_items=[]

def quit():
    import sys
    sys.exit()

