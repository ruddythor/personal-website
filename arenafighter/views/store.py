import collections
from django.shortcuts import render, redirect
from arenafighter.models.inventory import Inventory, Weapon, Armor, Potion
from arenafighter.models.character import Character

# TODO: DE-uglify this view function
def shop(request, store_level):
    potions = Potion.objects.exclude(inventory__isnull=False)
    weapons = Weapon.objects.exclude(inventory__isnull=False)
    armor = Armor.objects.exclude(inventory__isnull=False)
    if not potions:
        generate_items(store_level)
    if not armor:
        generate_armor(store_level)
    if not weapons:
        generate_weapons(store_level)
    potions = Potion.objects.exclude(inventory__isnull=False)
    weapons = Weapon.objects.exclude(inventory__isnull=False)
    armor = Armor.objects.exclude(inventory__isnull=False)
    potions = dict(collections.Counter([item.name for item in potions]))
    weapons = dict(collections.Counter([item.name for item in weapons]))
    armor = dict(collections.Counter([item.name for item in armor]))
    context = {'items': potions,
               'weapons': weapons,
               'armor': armor,
               }
    return render(request, 'store.html', context)


def character_inventory(request):
    character = Character.objects.get(id=request.user.profile.current_character_id)
    inventory = Inventory.objects.prefetch_related('items', 'armor', 'weapons').filter(character=character)[0]
    potions = dict(collections.Counter([item.name for item in inventory.potions.all()]))
    weapons = dict(collections.Counter([item.name for item in inventory.weapons.all()]))
    armor = dict(collections.Counter([item.name for item in inventory.armor.all()]))
    context = {'character': character,
               'items': potions,
               'weapons': weapons,
               'armor': armor,
               }
    return render(request, 'sell_items.html', context)


# TODO: combine these *_detail views to be better
def item_detail(request, name, store=False, sell=False):
    if store:
        object = Potion.objects.filter(name=name).filter(inventory_id=None)[0]
    elif sell:
        object = Potion.objects.filter(name=name).filter(inventory_id=request.user.profile.current_character.inventory.id)[0]
    else:
        object = Potion.objects.filter(name=name).filter(inventory_id=request.user.profile.current_character.inventory.id)[0]
    context = {'item': object,
               'store': store,
               'sell': sell,
               }
    return render(request, 'item.html', context)


def armor_detail(request, name, store=False, sell=False):
    if store:
        object = Armor.objects.filter(name=name).filter(inventory_id=None)[0]
    elif sell:
        object = Armor.objects.filter(name=name).filter(inventory_id=request.user.profile.current_character.inventory.id)[0]
    else:
        object = Armor.objects.filter(name=name).filter(inventory_id=request.user.profile.current_character.inventory.id)[0]
    context = {'item': object,
               'store': store,
               'sell': sell,
               }
    return render(request, 'item.html', context)


def weapon_detail(request, name, store=False, sell=False):
    if store:
        object = Weapon.objects.filter(name=name).filter(inventory_id=None)[0]
    elif sell:
        object = Weapon.objects.filter(name=name).filter(inventory_id=request.user.profile.current_character.inventory.id)[0]
    else:
        object = Weapon.objects.filter(name=name).filter(inventory_id=request.user.profile.current_character.inventory.id)[0]
    context = {'item': object,
               'store': store,
               'sell': sell,
               }
    return render(request, 'item.html', context)

def buy(request, item_type, id):
    if item_type == 'armor':
        object = Armor.objects.get(id=id)
    elif item_type == 'weapon':
        object = Weapon.objects.get(id=id)
    elif item_type == 'potion':
        object = Potion.objects.get(id=id)
    request.user.profile.current_character.purchase(object)
    return redirect('store')


def sell(request, item_type, id):
    if item_type == 'armor':
        object = Armor.objects.get(id=id)
    elif item_type == 'weapon':
        object = Weapon.objects.get(id=id)
    elif item_type == 'potion':
        object = InventoryItem.objects.get(id=id)
    request.user.profile.current_character.sell(object)
    return redirect('store')



def generate_items(store_level):
    if store_level == 1:
        for x in range(0, 10):
            potion = Potion(name='Health Potion', description='potion', buy_value=10, sell_value=2)
            potion.save()

def generate_weapons(store_level):
    if store_level == 1:
        for x in range(0, 2):
            weapon = Weapon(name='Cutter', description='A basic sword', buy_value=12, sell_value=3, attack_value=1)
            weapon.save()
            weapon2 = Weapon(name='Kamikaze', description='A low-end sword', buy_value=20, sell_value=5, attack_value=2)
            weapon2.save()

def generate_armor(store_level):
    if store_level == 1:
        for x in range(0, 2):
            armor = Armor(name='The Protector', description='A basic set of armor, providing minimal protection', buy_value=14, sell_value=3)
            armor.save()
            armor2 = Armor(name='Gladatorius', description='Basic armor that provides a small amount of protection', buy_value=20, sell_value=5, defense_value=3)
            armor2.save()
