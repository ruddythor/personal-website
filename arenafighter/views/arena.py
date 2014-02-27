#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
from arenafighter.models.player import playerone
from arenafighter.models.enemy import Enemy, random_enemy
from arenafighter.utils import dice

def fight(request):
    random_enemy('weak')


    while opponent.current_hp > 0 or playerone.current_hp > 0:
        player_initiative = dice.roll(1, 21)
        opponent_initiative = dice.roll(1, 21)
        
        if player_initiative > opponent_initiative:
            player_attacks(playerone, opponent)

            if opponent.current_hp <= 0:
                won_fight(playerone, opponent)
                break

            enemy_attacks(opponent, playerone)
            if playerone.current_hp <= 0:
                playerone.current_hp = playerone.hpmax
                break

        elif opponent_initiative>player_initiative:
            print "Opponent goes first."
            enemy_attacks(opponent, playerone)
            if playerone.current_hp <= 0:
                playerone.current_hp = playerone.hpmax

            player_attacks(playerone, opponent)
            if opponent.current_hp <= 0:
                won_fight(playerone, opponent)
                break



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
    return player


def check_for_levelup(player):
    if player.xp >= player.next_levelup:
        player.level += 1
        player.hpmax += int(playerone.hpmax*.15)
        player.next_levelup = int(player.next_levelup*.2 + player.next_levelup)
        player.xp = 0
        return player
    else:
        return player

# This defines an enemy strength definition where the key is the relative strength of the enemy
# and the value is a dict of attributes for that enemy, where the dict key corresponds to an attribute
# of Enemy(), making it easy to create random Enemy objects based on this dict



