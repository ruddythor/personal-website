from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from arenafighter.forms import CreateCharacterForm, LoginForm
from arenafighter.models.character import Character
from django.contrib.auth import authenticate, login, logout
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon
from arenafighter.utils import dice
import collections


def home(request):
    characters = []
    if request.user.is_authenticated():
        characters = Character.objects.filter(created_by=request.user.get_profile())

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
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
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

# TODO: clean this view up a bit
def info(request, id):
    try:
        character = Character.objects.get(id=id)
        inventory = Inventory.objects.prefetch_related('items', 'armor', 'weapons').filter(character=character)[0]
        items = dict(collections.Counter([item.name for item in inventory.items.all()]))
        weapons = dict(collections.Counter([item.name for item in inventory.weapons.all()]))
        armor = dict(collections.Counter([item.name for item in inventory.armor.all()]))
        context = {'character': character,
                   'current_character': request.user.get_profile().current_character,
                   'items': items,
                   'weapons': weapons,
                   'armor': armor,
                   }
    except:
        return redirect('home')
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

def equip(request, item_type, item_id):
    character = Character.objects.get(id=request.user.profile.current_character_id)
    character.equip(item_type, item_id)
    return redirect('home')

def go_to_arena(request):
    context = {}
    return render(request, 'arena.html', context)


