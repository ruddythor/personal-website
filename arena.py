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
    opponent=random.choice(enemylist)
    enemy_hp=opponent.hpmax
    enemy_defend=opponent.defend()
    playerone_hp=rpg.playerone.hpmax
    print "Rat's HP"
    print opponent.hpmax
    your_defend=rpg.playerone.defend()
    enemy_attack=opponent.attack()
    your_attack=rpg.playerone.attack()
    while enemy_hp or playerone_hp >=0:
        your_attack=your_attack-enemy_defend
        enemy_attack=enemy_attack-your_defend
        if enemy_attack>=your_defend:
            playerone_hp=playerone_hp-enemy_attack
        elif your_attack>=enemy_defend:
            enemy_hp=enemy_hp-your_attack
        else:
            enemy_attack=opponent.attack()
        print enemy_attack
        print "This is the enemy's hp", enemy_hp
        print "This is your hp", playerone_hp

        if enemy_hp<=0:
            print "You defeated the enemy"
            print "enemy's hp", enemy_hp
            print "Your hp", playerone_hp
            rpg.main_menu()
            break
        #will need a function to divvy out rewards if you win
        elif playerone_hp<=0:
            print "You died"
            print "enemy's hp", enemy_hp
            print "Your hp", playerone_hp
            break
