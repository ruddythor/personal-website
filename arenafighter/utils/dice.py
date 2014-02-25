#!/usr/bin/env python
'''
Created on Sep 27, 2012

@author: josh
'''
import random

def __str__(self):
    return 'Dieroll'
def __repr__(self):
    return 'Dieroll'

def roll(dice, sides):
    total=0
    for x in range(1, dice+1):
        total += random.randrange(1, sides+1)
    return int(total)
