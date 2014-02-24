#!/usr/bin/env python
'''
Created on Oct 3, 2012

@author: josh
'''
import player
import store
import arena
import sys

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
        store.main()
    elif player_choice==2:
        arena.fight()
    elif player_choice==3:
        info()
    elif player_choice==4:
        change_equipment()
    elif player_choice==5:
        endgame()
    else:
        main()


def change_equipment():
    print """\n\n\n\n\nThe following items are equippable by you:"""
    print
    for index, item in enumerate(player.playerone.equipment):
        print "\t %r: %r" % (int(index)+1, item)

    print "\nWhat would you like to equip?"
    equip_this=input(">>")
    player.playerone.equip(player.playerone.equipment[equip_this-1])
    main()

def info():
    print ("This is your character's information:\n\tName: ", player.playerone.Name,
          "\n\tlevel: ", player.playerone.level, 
          "\n\thpmax: ", player.playerone.hpmax, 
          "\n\tbase attack: ", player.playerone.base_attack, 
          "\n\tbase defense vale: ", player.playerone.base_defense, 
          "\n\tgold: ", player.playerone.gold)
    player.playerone.display_equipped()
#    for item in player.playerone.equipped_items:
#        print "\t", item, "attack value: ", item.attack_value, "defense value: ", item.defense_value
    player.playerone.display_inventory()
    advance_screen=raw_input("PRESS ENTER TO ADVANCE TO MAIN MENU\n\n")
    main()

def endgame():
    global gameover
    gameover=True
    sys.exit()
#    return gameover
