'''
created on October 28, 2012


@author matthew
'''



import random

class Die:

	def __init__(self):
        	pass
	def __str__(self):
            return 'Dieroll'
        def __repr__(self):
            return 'Dieroll'


	def roll(self, num, sides):
		total = 0		
		while num > 0:
			total += random.randint(1, sides)
			num -= 1
		return total
