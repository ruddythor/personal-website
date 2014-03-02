#!/usr/bin/env python
'''
Created on Oct 2, 2012

@author: josh
'''
from django.shortcuts import render, redirect
from arenafighter.models.character import Character
from arenafighter.models.inventory import Inventory, InventoryItem, Weapon, Armor

def shop(request):
    items = InventoryItem.objects.all()
    weapons = Weapon.objects.all()
    armors = Armor.objects.all()
    context = {'items': items,
               'weapons': weapons,
               'armors': armors,
               }
    return render(request, 'store.html', context)

def item_detail(request, id):
    object = InventoryItem.objects.get(id=id)
    context = {
            'item': object,
            }

    return render(request, 'item.html', context)


def armor_detail(request, id):
    object = Armor.objects.get(id=id)
    context = {
            'item': object,
            }

    return render(request, 'item.html', context)


def weapon_detail(request, id):
    object = Weapon.objects.get(id=id)
    context = {
            'item': object,
            }

    return render(request, 'item.html', context)

def buy_armor(request, id):
    object = Armor.objects.get(id=id)
    character = Character.objects.get(id=request.user.profile.current_character.id)
    character.inventory.armors.add(object)
    character.gold -= object.buy_value
    character.save()
    context = {
            'item': object,
            }
    return redirect('store')

def buy_weapon(request, id):
    object = Weapon.objects.get(id=id)
    character = Character.objects.get(id=request.user.profile.current_character.id)
    character.inventory.weapons.add(object)
    character.gold -= object.buy_value
    character.save()
    context = {
            'item': object,
            }
    return redirect('store')


def buy_item(request, id):
    object = InventoryItem.objects.get(id=id)
    character = Character.objects.get(id=request.user.profile.current_character.id)
    character.inventory.items.add(object)
    character.gold -= object.buy_value
    character.save()
    context = {
            'item': object,
            }
    return redirect('store')




