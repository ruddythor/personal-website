#!/usr/bin/env python
'''
Created on Oct 3, 2012

@author: josh
'''
import character
import equipmentlist

global available_items
available_items={1:equipmentlist.dagger, 2:equipmentlist.shortsword, 3:equipmentlist.longsword, 4:equipmentlist.lightarmor, 5:equipmentlist.heavyarmor}


playerone=character.Player("Charles", 1)
playerone.add(equipmentlist.longsword)
playerone.add(equipmentlist.shortsword)
playerone.add(equipmentlist.lightarmor)
playerone.add(equipmentlist.heavyarmor)
playerone.equip(equipmentlist.shortsword)
playerone.equip(equipmentlist.lightarmor)

