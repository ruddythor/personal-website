#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
import equipment
import random


def fight():
    import rpg
    from enemylist import enemylist
# PICKS AN ENEMY FROM ENEMYLIST FILE
    opponent=random.choice(enemylist)
    
    enemy_hp=opponent.hpmax
    enemy_defend=opponent.defend()
    playerone_hp=rpg.playerone.hpmax
    your_defend=rpg.playerone.defend()
   
    print "You are fighting "+opponent.Name, "\n\topponent's max HP:", opponent.hpmax, "\n\tYour HP:", rpg.playerone.hpmax
    while enemy_hp or playerone_hp >=0:
        enemy_attack=opponent.attack()
        your_attack=rpg.playerone.attack()
#problem with this is that both attack at once, so you can both die. need to fix that=====================
#=========================================================================================================
        for item in rpg.playerone.equipped_items:
            print item, item.attack_value
        print
        print
        if enemy_attack>your_defend:
            print enemy_attack, "enemy attack before defend"
            enemy_attack=enemy_attack-your_defend
            print enemy_attack, "<--ENEMY ATTACK VAL (after factoring defense) WAS"
            print enemy_defend, "<--ENEMY DEF VAL"
            playerone_hp=playerone_hp-enemy_attack
        if your_attack>enemy_defend:
            your_attack=your_attack-enemy_defend
            print your_attack, "<--YOUR ATTACK (after factoring defnese) VAL WAS"
            print your_defend, "<--YOUR DEFENSE VAL"
            enemy_hp=enemy_hp-your_attack
        else:
            enemy_attack=opponent.attack()
        print "Enemy HP:\t\t", enemy_hp
        print "Your HP:\t\t", playerone_hp, "\n\nEND OF ROUND\n--------------"

        if enemy_hp<=0:
            print "You defeated the enemy"
            print "enemy's hp", enemy_hp
            print "Your hp", playerone_hp
            rpg.playerone.xp+=opponent.xp_value
            rpg.playerone.renown+=opponent.renown_value
            print rpg.playerone.renown, rpg.playerone.xp
            
            
            rpg.main_menu()
            break
        #will need a function to divvy out rewards if you win
        elif playerone_hp<=0:
            print "================You died================"
            print "\tenemy's hp\t\t", enemy_hp
            print "\tYour hp\t\t", playerone_hp
            rpg.main_menu()
            break
