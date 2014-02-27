#!/usr/bin/env python
'''
Created on Oct 3, 2012

@author: josh
'''
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from arenafighter.forms import CreateCharacterForm, LoginForm
from arenafighter.models.character import Player
from django.contrib.auth import authenticate, login, logout
from arenafighter.models.profile_model import Profile
from django.forms.models import inlineformset_factory


def home(request):
    characters = Player.objects.all()
    if request.POST:

        form = CreateCharacterForm(request.POST)
        if form.is_valid():
            player = Player(name=request.POST['name'])
            request.user.profile.current_character = player
            print player
            player.save()
            request.user.profile.save()
            return redirect('home')
    else:
        form = CreateCharacterForm()

    context = {
        'form': form,
        'characters': characters,
    }
    return render(request, 'home.html', context)

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')


def info(request, id):
    try:
        player = Player.objects.get(id=id)
    except:
        return redirect('home')
    context = {
        'player': player,
        'request': request,
        'level': player.level,
        'hpmax': player.hpmax,
        'base_attack': player.base_attack,
        'base_defense': player.base_defense,
        'gold': player.gold,
    }
    return render(request, 'info.html', context)

def delete(request, id):
    player = Player.objects.get(id=id)
    player.delete()
    return redirect('home')

def play_as_character(request, id):
    if request.user.profile:
        player = Player.objects.get(id=id)
        player.save()
        request.user.profile.current_character = player
        player.current_player.add(request.user.profile)
        request.user.profile.save()
        return redirect('home')
    else:
        profile = Profile(user=request.user)
        profile.save()
        request.user.profile.current_character = Player.objects.get(id=id)
        request.user.save()
    return render(request, 'home.html')

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



