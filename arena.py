#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
from player import playerone
import random
from dice import Die

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
                won_fight(playerone, opponent)
                break

            enemy_attacks(opponent, playerone)
            if playerone.current_hp <= 0:
                playerone.current_hp = playerone.hpmax
                print "You were defeated. Returning to main menu"
                break
            print "Your hp: ", playerone.current_hp, "Enemy's hp: ", opponent.current_hp
        
        elif opponent_initiative>player_initiative:
            print "Opponent goes first."
            enemy_attacks(opponent, playerone)
            if playerone.current_hp <= 0:
                playerone.current_hp = playerone.hpmax
                print"You were defeated. Returning to main menu"

            player_attacks(playerone, opponent)
            if opponent.current_hp <= 0:
                won_fight(playerone, opponent)
                break
            print "Your hp: ", playerone.current_hp, "Enemy's hp: ", opponent.current_hp
        print "END OF TURN\n-----------------------------"



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


def won_fight(player, opponent):
    player.xp += opponent.xp_value
    player.gold += opponent.gold
    player.renown += opponent.renown_value
    check_for_levelup(player)
    player.current_hp = player.hpmax
    print "Your XP:", player.xp, "\nyou defeated the enemy, returning to main menu"



def check_for_levelup(player):
    print "about to check for level up"
    if player.xp >= player.next_levelup:
        print "Checking for level up"
        player.level += 1
        player.hpmax += int(playerone.hpmax*.15)
        player.next_levelup = int(player.next_levelup*.2 + player.next_levelup)
        print "**** You leveled up! ****\n your new level is: ", player.level, "your next level-up in: ", player.next_levelup, "your new hp is: ", player.hpmax
        player.xp = 0













