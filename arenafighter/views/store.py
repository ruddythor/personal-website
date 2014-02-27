#!/usr/bin/env python
'''
Created on Oct 2, 2012

@author: josh
'''
from django.shortcuts import render, redirect
from arenafighter.models.character import Player
from arenafighter.models.equipment import Inventory, InventoryItem, Weapon, Armor

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
    player = Player.objects.get(id=request.user.profile.current_character.id)
    player.inventory.armors.add(object)
    player.gold -= object.buy_value
    player.save()
    context = {
            'item': object,
            }
    return redirect('store')

def buy_weapon(request, id):
    object = Weapon.objects.get(id=id)
    player = Player.objects.get(id=request.user.profile.current_character.id)
    player.inventory.weapons.add(object)
    player.gold -= object.buy_value
    player.save()
    context = {
            'item': object,
            }
    return redirect('store')


def buy_item(request, id):
    object = InventoryItem.objects.get(id=id)
    player = Player.objects.get(id=request.user.profile.current_character.id)
    player.inventory.items.add(object)
    player.gold -= object.buy_value
    player.save()
    context = {
            'item': object,
            }
    return redirect('store')






def buy():


    for key in player.available_items:
        print "\t", key, ":", player.available_items[key], "\t", player.available_items[key].buy_value, "gold"
    print "You have %i gold.\nEnter the number of the item you'd like to purchase." % player.playerone.gold
    purchase_item=input(">>")

    if player.available_items[purchase_item].buy_value<=player.playerone.gold:
        player.playerone.add(player.available_items[purchase_item])
        player.playerone.gold=player.playerone.gold-player.available_items[purchase_item].buy_value
        print "You now have %i gold" % player.playerone.gold
#    menus.main()


def sell():
    print "\n\n\n\n\nYou have the following items to sell:"
    i=1
    for x in player.playerone.equipment:
        print "\t", i, ":", x, "\t", x.sell_value, "gold"
        i+=1
    print "Enter the number of the item you'd like to sell."
    sell_item=input(">>")
    item_sold=player.playerone.equipment[sell_item-1]
    player.playerone.gold+=item_sold.sell_value
    if item_sold in player.playerone.equipped_items:
        player.playerone.unequip(item_sold)
    player.playerone.drop(item_sold)
#    menus.main()
