from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from arenafighter.forms import CreateCharacterForm, LoginForm
from arenafighter.models.character import Character
from arenafighter.models.profile_model import User
from django.contrib.auth import authenticate, login, logout
from arenafighter.models.profile_model import Profile
from django.forms.models import inlineformset_factory
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon
import collections


def home(request):
    characters = Character.objects.all()
    if request.POST:

        form = CreateCharacterForm(request.POST)
        if form.is_valid():
            character = Character(name=request.POST['name'])
            request.user.profile.current_character = character
            inventory = Inventory()
            character.save()
            request.user.profile.save()
            inventory.character = character
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


def info(request, id):
    try:
        character = Character.objects.select_related('equipped_armor', 'equipped_armor__inventory', 'profile__user', 'user__profile', 'user').filter(id=id)[0]
        inventory_items = InventoryItem.objects.filter(inventory=character)
        inventory_weapons = Weapon.objects.prefetch_related('inventory__character').filter(inventory=character)
        inventory_armor = Armor.objects.filter(inventory=character)
        item_count = dict(collections.Counter([item.name for item in inventory_items]))
        weapons_count = dict(collections.Counter([item.name for item in inventory_weapons]))
        armor_count = dict(collections.Counter([item.name for item in inventory_armor]))
        context = {'character': character,
                   'current_character': request.user.get_profile().current_character,
                   'items': inventory_items,
                   'armor': inventory_armor,
                   'weapons': inventory_weapons,
                   'item_count': item_count,
                   'weapons_count': weapons_count,
                   'armor_count': armor_count,
                   }
    except:
        return redirect('home')
    return render(request, 'info.html', context)

def delete(request, id):
    character = Character.objects.get(id=id)
    character.delete()
    return redirect('home')

def play_as_character(request, id):
#    if request.user.profile:
    character = Character.objects.get(id=id)
    character.current_character.add(request.user.profile)
    character.save()
    return redirect('home')
#    else:
#        profile = Profile(user=request.user)
#        profile.save()
#        request.user.profile.current_character = Character.objects.get(id=id)
#        request.user.save()
#    return render(request, 'home.html')

def go_to_store(request):
    context = {}
    return render(request, 'store.html', context)

def equip(request, item_type, item_id):
    character = Character.objects.get(id=request.user.profile.current_character_id)
    if item_type == 'Weapon':
        weapon = Weapon.objects.get(id=item_id)
        character.equip_weapon(weapon)
    elif item_type == 'InventoryItem':
        item = InventoryItem.objects.get(id=item_id)
        character.equip_item(item)
    elif item_type == 'Armor':
        armor = Armor.objects.get(id=item_id)
        character.equip_armor(armor)
    return redirect('home')

def go_to_arena(request):
    if request.session.get('message'):
        message = request.session.get('message')
        context = {'message': message}
        del(request.session['message'])
    else:
        context = {}
    return render(request, 'arena.html', context)


