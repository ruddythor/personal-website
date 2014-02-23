#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
from player import playerone
import random
from dice import Die

global level_threshhold
level_threshhold=100
def fight():
    from enemylist import enemylist
# PICKS AN ENEMY FROM ENEMYLIST FILE
    opponent=random.choice(enemylist)
    global enemy_hp, playerone_hp
    opponent.hpmax=opponent.hpmax
    enemy_hp=opponent.hpmax
    playerone_hp= playerone.hpmax

    print "You are fighting "+opponent.Name, "\n\tOpponent's max HP:", opponent.hpmax, "\n\tYour HP:", playerone.hpmax

    while enemy_hp > 0 or playerone_hp > 0:
        dice = Die()
        player_initiative = dice.roll(1, 21)
        opponent_initiative = dice.roll(1, 21)
        
        if player_initiative > opponent_initiative:
            print "Player goes first."
            playerone_attack_check(your_attack, enemy_defend, enemy_hp, playerone_hp)
            if enemy_hp<=0:
                playerone.xp+=opponent.xp_value
                playerone.gold+=opponent.gold
                playerone.renown+=opponent.renown_value
                check_for_levelup()
                print playerone.xp, "\nyou defeated the enemy, returning to main menu"
                break

            enemy_attack_check(enemy_attack, your_defend, playerone_hp, enemy_hp)
            if playerone_hp<=0:
                print "You were defeated. Returning to main menu"
#                menus.main()
                break
            print "Your hp: ", playerone_hp, "Enemy's hp: ", enemy_hp
        
        elif opponent_initiative>player_initiative:
            print "Opponent goes first."
            enemy_attack_check(enemy_attack, your_defend, playerone_hp, enemy_hp)
            if playerone_hp<=0:
                print"You were defeated. Returning to main menu"
#                menus.main()
            playerone_attack_check(your_attack, enemy_defend, enemy_hp, playerone_hp)
            if enemy_hp<=0:
                playerone.xp+=opponent.xp_value
                playerone.gold+=opponent.gold
                playerone.renown+=opponent.renown_value
                check_for_levelup()
                print playerone.xp, "\nyou defeated the enemy, returning to main menu"
#                menus.main()
                break
            print "Your hp: ", playerone_hp, "Enemy's hp: ", enemy_hp
        print "END OF TURN\n-----------------------------"
#    menus.main()

def enemy_attack_check(enemy_attack, your_defend, player_hp, enemy_hp):
    global playerone_hp
    if enemy_attack>your_defend:
        print "opponent lands attack"
        enemy_attack=enemy_attack-your_defend
        playerone_hp=playerone_hp-enemy_attack
        print playerone_hp

def playerone_attack_check(your_attack, enemy_defend, enem_hp, playerone_hp):
    global enemy_hp
    if your_attack>enemy_defend:
        print "player lands attack"
        your_attack=your_attack-enemy_defend
        enemy_hp=enemy_hp-your_attack
        print enemy_hp

def check_for_levelup():
    print "about to check for level up"
    global level_threshhold
    if playerone.xp>=level_threshhold:
        print "Checking for level up"
        playerone.level+=1
        playerone.hpmax+=int(playerone.hpmax*.15)
        level_threshhold=int(level_threshhold*.2+level_threshhold)
        print "**** You leveled up! ****\n your new level is: ", playerone.level, "your new level threshhold", level_threshhold, "your new hp is: ", playerone.hpmax
        playerone.xp=0



def player_attacks():
    pass











