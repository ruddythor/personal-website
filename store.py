#!/usr/bin/env python
'''
Created on Oct 2, 2012

@author: josh
'''
import player
import menus

def main():
    print "\n\n\n\n\nEnter 1 to buy something. Enter 2 to sell something."
    buy_or_sell=input("\n>>")
    if buy_or_sell==1:
        buy()
    elif buy_or_sell==2:
        sell()


def buy():
    global available_items
    print "\n\n\n\n\nThe following items are available for purchase:"
    for key in player.available_items:
        print "\t", key, ":", player.available_items[key], "\t", player.available_items[key].buy_value, "gold"
    print "You have %i gold.\nEnter the number of the item you'd like to purchase." % player.playerone.gold
    purchase_item=input(">>")

    if player.available_items[purchase_item].buy_value<=player.playerone.gold:
        player.playerone.add(player.available_items[purchase_item])
        player.playerone.gold=player.playerone.gold-player.available_items[purchase_item].buy_value
        print "You now have %i gold" % player.playerone.gold
    #menus.main()


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
    #menus.main()
