#!/usr/bin/env python
'''
Created on Oct 2, 2012

@author: josh
'''
import equipment
			    #attack_value, defense_value, name,                   description,              is_armor, buy_value, sell_value
longsword=equipment.Equipment(    10,             0, "long sword", "A bad-ass slayer of women and small men", False,       50,       15)
shortsword=equipment.Equipment(7, 0, "short sword", "A not-so-bad-ass slayer of women and small men", False, 25, 7)
dagger=equipment.Equipment(4, 0, "dagger", "A small dagger, capable of killing someone, but only if you get really close to them.", False, 15, 4)
lightarmor=equipment.Equipment(0, 5, "light armor", "A simple piece of armor that barely protects you. It is very simple looking.", True, 65, 20)
heavyarmor=equipment.Equipment(0,15, "heavy armor", "A complex piece of armor that protects you strongly.", True, 100, 25)
