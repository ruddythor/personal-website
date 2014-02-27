#!/usr/bin/env python
'''
Created on Oct 2, 2012

@author: josh
'''
from django.shortcuts import render, redirect
from arenafighter.models.character import Player

def shop(request):

    context = {}
    return render(request, 'store.html', context)


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
