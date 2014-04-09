from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from arenafighter.forms import CreateCharacterForm, LoginForm, SignupForm
from arenafighter.models.character import Character
from django.contrib.auth import authenticate, login, logout
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon
from arenafighter.utils import dice
import collections


def home(request):
    characters = []
    if request.user.is_authenticated():
        characters = Character.objects.filter(created_by=request.user.profile.id)

    if request.POST:
        form = CreateCharacterForm(request.POST)
        if form.is_valid():
            hp = dice.roll(18, 5)
            character = Character(name=request.POST['name'], hpmax=hp, current_hp=hp)
            request.user.profile.created_characters.add(character)
            character.save()
            inventory = Inventory(character=character)
            inventory.save()
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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
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
        character = Character.objects.get(id=id)
        items = dict(collections.Counter([item for item in character.items]))
        equipped_items = dict(collections.Counter([item for item in character.equipped_items]))
        context = {'character': character,
                   'current_character': request.user.profile.current_character,
                   'items': items,
                   'equipped_items': equipped_items,
                   }
    except:
        return redirect('player_info')

    return render(request, 'info.html', context)

def delete(request, id):
    character = Character.objects.get(id=id)
    character.delete()
    return redirect('home')

def play_as_character(request, id):
    character = Character.objects.get(id=id)
    character.profile.add(request.user.profile)
    character.save()
    return redirect('player_info', character.id)

def go_to_store(request):
    context = {}
    return render(request, 'store.html', context)

def go_to_arena(request):
    context = {}
    return render(request, 'arena.html', context)


def equip_weapon(request, weapon_id):
    if request.POST:
        weapon = Weapon.objects.get(id=weapon_id)
        request.user.profile.current_character.equip(weapon)
    return redirect('player_info', request.user.profile.current_character_id)

def equip_armor(request, armor_id):
    if request.POST:
        armor = Armor.objects.get(id=armor_id)
        request.user.profile.current_character.equip(armor)
    return redirect('player_info', request.user.profile.current_character_id)

def unequip_weapon(request, armor_id):
    if request.POST:
        weapon = Weapon.objects.get(id=armor_id)
        request.user.profile.current_character.unequip(weapon)
    return redirect('player_info', request.user.profile.current_character_id)

def unequip_armor(request, armor_id):
    if request.POST:
        armor = Armor.objects.get(id=armor_id)
        request.user.profile.current_character.unequip(armor)
    return redirect('player_info', request.user.profile.current_character_id)






