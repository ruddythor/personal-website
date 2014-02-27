#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
from django.shortcuts import render, redirect
from arenafighter.models.character import Player
from arenafighter.models.enemy import Enemy, generate_enemy
from arenafighter.utils import dice

def fight(request):
    enemy = generate_enemy('weak')
    print enemy
    print request.user.profile.current_character.current_hp
    character = Player.objects.get(id=request.user.profile.current_character.id)

    while enemy.current_hp > 0 or player.current_hp > 0:
        message = "Looks like you're both about evenly matched"
        player_initiative = dice.roll(1, 21)
        opponent_initiative = dice.roll(1, 21)
        if player_initiative > opponent_initiative:
            player_attacks(character, enemy)
            if enemy.current_hp <= 0:
                won_fight(character, enemy)
                request.session['message'] = "You really showed that ass who's boss!! Good job, mate"
                character.fights_won += 1
                character.save()
                return redirect('arena')
            enemy_attacks(enemy, character)
            if character.current_hp <= 0:
                character.current_hp = character.hpmax
                request.session['message'] = "Looks like you lost, boss. Better luck next time. Our healers have fixed you up from the fight."
                character.fights_lost += 1
                character.save()
                return redirect('arena')
        elif opponent_initiative > player_initiative:
            enemy_attacks(enemy, character)
            if character.current_hp <= 0:
                character.current_hp = character.hpmax
                request.session['message'] = "Looks like you lost, boss. Better luck next time. Our healers have fixed you up from the fight."
                character.fights_lost += 1
                character.save()
                return redirect('arena')
            player_attacks(character, enemy)
            if enemy.current_hp <= 0:
                won_fight(character, enemy)
                request.session['message'] = "You really showed that ass who's boss!! Good job, mate"
                character.fights_won += 1
                character.save()
                return redirect('arena')

    context = {
        'enemy': enemy,
        'message': message,
    }
    return render(request, 'fight.html', context)



def enemy_attacks(enemy, player):
    if enemy.attack() > player.defense_value():
        attack_value = enemy.attack() - player.defense_value()
        player.current_hp -= attack_value
        return player

def player_attacks(player, enemy):
    if player.attack() > enemy.defense_value():
        attack_value = player.attack() - enemy.defense_value()
        enemy.current_hp -= attack_value
        return enemy


def won_fight(player, opponent):
    player.xp += opponent.xp_value
    player.gold += opponent.gold
    player.renown += opponent.renown_value
    check_for_levelup(player)
    player.current_hp = player.hpmax
    player.save()
    return player


def check_for_levelup(player):
    if player.xp >= player.next_levelup:
        player.level += 1
        player.hpmax += int(playerone.hpmax*.15)
        player.next_levelup = int(player.next_levelup*.2 + player.next_levelup)
        player.xp = 0
        player.save()
        return player
    else:
        return player

# This defines an enemy strength definition where the key is the relative strength of the enemy
# and the value is a dict of attributes for that enemy, where the dict key corresponds to an attribute
# of Enemy(), making it easy to create random Enemy objects based on this dict



