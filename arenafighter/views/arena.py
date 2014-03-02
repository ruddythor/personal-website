#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
from django.shortcuts import render, redirect
from arenafighter.models.character import Character
from arenafighter.models.enemy import Enemy, generate_enemy
from arenafighter.utils import dice

def fight(request):
    enemy = generate_enemy('weak')
    character = Character.objects.get(id=request.user.profile.current_character.id)

    while enemy.current_hp > 0 or character.current_hp > 0:
        message = "Looks like you're both about evenly matched"
        character_initiative = dice.roll(1, 21)
        opponent_initiative = dice.roll(1, 21)
        if character_initiative > opponent_initiative:
            character_attacks(character, enemy)
            if enemy.current_hp <= 0:
                won_fight(character, enemy)
                request.session['message'] = "You really showed that ass who's boss!! Good job, mate"
                return redirect('arena')
            enemy_attacks(enemy, character)
            if character.current_hp <= 0:
                character.current_hp = character.hpmax
                request.session['message'] = "Looks like you lost, boss. Better luck next time. Our healers have fixed you up from the fight."
                character.fights_lost += 1
                character.save()
                return redirect('arena')
        elif opponent_initiative > character_initiative:
            enemy_attacks(enemy, character)
            if character.current_hp <= 0:
                character.current_hp = character.hpmax
                request.session['message'] = "Looks like you lost, boss. Better luck next time. Our healers have fixed you up from the fight."
                character.fights_lost += 1
                character.save()
                return redirect('arena')
            character_attacks(character, enemy)
            if enemy.current_hp <= 0:
                won_fight(character, enemy)
                request.session['message'] = "You really showed that ass who's boss!! Good job, mate"
                return redirect('arena')

    context = {
        'enemy': enemy,
        'message': message,
    }
    return render(request, 'fight.html', context)



def enemy_attacks(enemy, character):
    if enemy.attack() > character.defense_value():
        attack_value = enemy.attack() - character.defense_value()
        character.current_hp -= attack_value
        return character

def character_attacks(character, enemy):
    if character.attack() > enemy.defense_value():
        attack_value = character.attack() - enemy.defense_value()
        enemy.current_hp -= attack_value
        return enemy


def won_fight(character, opponent):
    character.xp += opponent.xp_value
    character.gold += opponent.gold
    character.renown += opponent.renown_value
    check_for_levelup(character)
    character.current_hp = character.hpmax
    character.fights_won += 1
    character.save()
    return character


def check_for_levelup(character):
    if character.xp >= character.next_levelup:
        character.level += 1
        character.hpmax += int(character.hpmax*.15)
        character.next_levelup = int(character.next_levelup*.2 + character.next_levelup)
        character.xp = 0
        character.save()
        return character
    else:
        return character

# This defines an enemy strength definition where the key is the relative strength of the enemy
# and the value is a dict of attributes for that enemy, where the dict key corresponds to an attribute
# of Enemy(), making it easy to create random Enemy objects based on this dict



