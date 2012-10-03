#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
import player
import random
#import menuclass

def fight():
    level_threshhold=100
    from enemylist import enemylist
# PICKS AN ENEMY FROM ENEMYLIST FILE
    opponent=random.choice(enemylist)
    
    enemy_hp=opponent.hpmax
    enemy_defend=opponent.defend()
    playerone_hp=player.playerone.hpmax
    your_defend=player.playerone.defend()
    print "You are fighting "+opponent.Name, "\n\topponent's max HP:", opponent.hpmax, "\n\tYour HP:", player.playerone.hpmax
    while enemy_hp or playerone_hp >=0:
        enemy_attack=opponent.attack()
        your_attack=player.playerone.attack()
#problem with this is that both attack at once, so you can both die. need to fix that=====================
#=========================================================================================================
        for item in player.playerone.equipped_items:
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
        print "Enemy HP:\t\t", enemy_hp
        print "Your HP:\t\t", playerone_hp, "\n\nEND OF ROUND\n--------------"

        if enemy_hp<=0:
            print "You defeated the enemy"
            print "enemy's hp", enemy_hp
            print "Your hp", playerone_hp
            player.playerone.xp+=opponent.xp_value
            player.playerone.renown+=opponent.renown_value
            print player.playerone.renown, player.playerone.xp
            if player.playerone.xp>=level_threshhold:
                player.playerone.level+=1
                print "**** You leveled up! ****"
                player.playerone.hpmax+=player.playerone.hpmax*.15#NEED TO ROUND UP!!!!
                level_threshhold=level_threshhold*.2+level_threshhold
            import menus
            menus.main()        
            break
        #will need a function to divvy out rewards if you win
        elif playerone_hp<=0:
            print "================You died================"
            print "\tenemy's hp\t\t", enemy_hp
            print "\tYour hp\t\t", playerone_hp
            break
