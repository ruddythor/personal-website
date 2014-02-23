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


    print "You are fighting "+opponent.Name, "\n\tOpponent's max HP:", opponent.hpmax, "\n\tYour HP:", playerone.current_hp

    while opponent.current_hp > 0 or playerone.current_hp > 0:
        dice = Die()
        player_initiative = dice.roll(1, 21)
        opponent_initiative = dice.roll(1, 21)
        
        if player_initiative > opponent_initiative:
            print "Player goes first."


            player_attacks(playerone, opponent)

            if opponent.current_hp <= 0:
                playerone.xp+=opponent.xp_value
                playerone.gold+=opponent.gold
                playerone.renown+=opponent.renown_value
                check_for_levelup()
                print playerone.xp, "\nyou defeated the enemy, returning to main menu"
                break

            enemy_attacks(opponent, playerone)
            if playerone.current_hp <= 0:
                print "You were defeated. Returning to main menu"
#                menus.main()
                break
            print "Your hp: ", playerone.current_hp, "Enemy's hp: ", opponent.current_hp
        
        elif opponent_initiative>player_initiative:
            print "Opponent goes first."
            enemy_attacks(opponent, playerone)
            if playerone.current_hp <= 0:
                print"You were defeated. Returning to main menu"
#                menus.main()
            player_attacks(playerone, opponent)
            if opponent.current_hp <= 0:
                playerone.xp+=opponent.xp_value
                playerone.gold+=opponent.gold
                playerone.renown+=opponent.renown_value
                check_for_levelup()
                print playerone.xp, "\nyou defeated the enemy, returning to main menu"
#                menus.main()
                break
            print "Your hp: ", playerone.current_hp, "Enemy's hp: ", opponent.current_hp
        print "END OF TURN\n-----------------------------"
#    menus.main()



def enemy_attacks(enemy, player):
    if enemy.attack() > player.defense_value():
        attack_value = enemy.attack() - player.defense_value()
        player.current_hp -= attack_value
        return player.current_hp

def player_attacks(player, enemy):
    if player.attack() > enemy.defense_value():
        attack_value = player.attack() - enemy.defense_value()
        enemy.current_hp -= attack_value
        return enemy.current_hp



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













