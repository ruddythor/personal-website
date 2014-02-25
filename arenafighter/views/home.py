#!/usr/bin/env python
'''
Created on Oct 3, 2012

@author: josh
'''

from django.shortcuts import render
from arenafighter.forms import CreateCharacterForm
from arenafighter.models.character import Player
import arenafighter.settings as settings



def home(request):
    characters = Player.objects.all()

    form = CreateCharacterForm()
    context = {
        'form': form,
        'characters': characters,
    }
    return render(request, 'home.html', context)


def go_to_store(request):
    context = {}
    return render(request, 'store.html', context)


def go_to_arena(request):
    context = {}
    return render(request, 'arena.html', context)


def change_equipment():
    print """\n\n\n\n\nThe following items are equippable by you:"""
    print
    for index, item in enumerate(player.playerone.equipment):
        print "\t %r: %r" % (int(index)+1, item)

    print "\nWhat would you like to equip?"
    equip_this=input(">>")
    player.playerone.equip(player.playerone.equipment[equip_this-1])
    main()


def info(request, id):
    player = Player.objects.get(id=id)
    context = {
        'level': player.level,
        'hpmax': player.hpmax,
        'base_attack': player.base_attack,
        'base_defense': player.base_defense,
        'gold': player.gold,
    }
    return render(request, 'info.html', context)



def main(request):
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
