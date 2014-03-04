import collections
from django.shortcuts import render, redirect
from arenafighter.models.character import Character
from arenafighter.models.inventory import Inventory, InventoryItem, Weapon, Armor

def shop(request, store_level):
    items = InventoryItem.objects.exclude(inventory__isnull=False)
    weapons = Weapon.objects.exclude(inventory__isnull=False)
    armor = Armor.objects.exclude(inventory__isnull=False)
    if not items:
        generate_items(store_level)
    if not armor:
        generate_armor(store_level)
    if not weapons:
        generate_weapons(store_level)
    items = InventoryItem.objects.exclude(inventory__isnull=False)
    weapons = Weapon.objects.exclude(inventory__isnull=False)
    armors = Armor.objects.exclude(inventory__isnull=False)
    items = dict(collections.Counter([item.name for item in items]))
    weapons = dict(collections.Counter([item.name for item in weapons]))
    armors = dict(collections.Counter([item.name for item in armors]))
    context = {'items': items,
               'weapons': weapons,
               'armors': armors,
               }
    return render(request, 'store.html', context)

def item_detail(request, name):
    object = InventoryItem.objects.filter(name=name).filter(inventory_id=None)[0]
    context = {
            'item': object,
            }

    return render(request, 'item.html', context)


def armor_detail(request, name):
    object = Armor.objects.filter(name=name).filter(inventory_id=None)[0]
    context = {
            'item': object,
            }

    return render(request, 'item.html', context)


def weapon_detail(request, name):
    object = Weapon.objects.filter(name=name).filter(inventory_id=None)[0]
    context = {'item': object,
               }

    return render(request, 'item.html', context)

def buy_armor(request, id):
    object = Armor.objects.get(id=id)
    character = Character.objects.get(id=request.user.profile.current_character_id)
    character.inventory.armor.add(object)
    character.gold -= object.buy_value
    character.save()
    context = {'item': object,
               }
    return redirect('store')

def buy_weapon(request, id):
    object = Weapon.objects.get(id=id)
    print object
    character = Character.objects.get(id=request.user.profile.current_character_id)
    character.inventory.weapons.add(object)
    character.gold -= object.buy_value
    character.save()
    context = {
            'item': object,
            }
    return redirect('store')


def buy_item(request, id):
    object = InventoryItem.objects.get(id=id)
    print object.name, object.id
    character = Character.objects.get(id=request.user.profile.current_character_id)
    character.inventory.items.add(object)
    character.gold -= object.buy_value
    character.save()
    context = {
            'item': object,
            }
    return redirect('store')



def generate_items(store_level):
    if store_level == 1:
        for x in range(0, 10):
            potion = InventoryItem(name='Health Potion', description='potion', buy_value=10, sell_value=2)
            potion.save()

def generate_weapons(store_level):
    if store_level == 1:
        for x in range(0, 2):
            weapon = Weapon(name='Cutter', description='A basic sword', buy_value=12, sell_value=3, attack_value=1)
            weapon.save()

def generate_armor(store_level):
    if store_level == 1:
        for x in range(0, 2):
            armor = Armor(name='The Protector', description='A basic set of armor, providing minimal protection', buy_value=14, sell_value=3)
            armor.save()
