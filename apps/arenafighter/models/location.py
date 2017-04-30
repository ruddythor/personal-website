'''
Created on Oct 1, 2012

@author: josh
'''
from apps.arenafighter.utils import dice
from django.db import models
from apps.arenafighter.models.enemy import Enemy, generate_enemy
from apps.arenafighter.models.enemy import enemy_strength_dict
from apps.arenafighter.models.inventory import Potion, Armor, Weapon


strength_dict = {
	1: 'weak',
	2: 'medium',
	3: 'strong',
	4: 'very strong',
	5: 'exceptionally strong',
	6: 'powerful',
	7: 'exceptionally powerful',
	8: 'ultimate',
}


class Location(models.Model):
#    character = models.ForeignKey('Character', default=None, related_name='location', blank=False, null=False)
    area_difficulty_level = models.IntegerField(default=1)
    name = models.TextField(default="Random Location")


    class Meta:
        app_label = 'arenafighter'


    def __unicode__(self):
        return self.name


    def spawn_enemy(self):
    	strength_dict = {
    		1: 'weak',
    		2: 'medium',
    		3: 'strong',
    		4: 'very strong',
    		5: 'exceptionally strong',
    		6: 'powerful',
    		7: 'exceptionally powerful',
    		8: 'ultimate',
    	}
    	strength = strength_dict[self.area_difficulty_level]
    	enemy = generate_enemy(strength)
    	return enemy



class Store(models.Model):
	location = models.ForeignKey('Location', default=None, related_name='stores', blank=True, null=True)

	class Meta:
		app_label = 'arenafighter'

	def __unicode__(self):
		return 'A Store'

	def generate_items(self):
		if self.location.area_difficulty_level == 1:
			for x in range(0, 10):
				potion = Potion(name='Health Potion', description='potion', buy_value=10, sell_value=2, shop=self)
				potion.save()
		elif self.location.area_difficulty_level == 2:
			potion = Potion(name='The Medium potion', description='A medium strength potion', buy_value=24, sell_value=15, shop=self)
			potion.save()

	def generate_weapons(self):
		if self.location.area_difficulty_level == 1:
			for x in range(0, 2):
				weapon = Weapon(name='Cutter', description='A basic sword', buy_value=12, sell_value=3, attack_value=1, shop=self)
				weapon.save()
				weapon2 = Weapon(name='Kamikaze', description='A low-end sword', buy_value=20, sell_value=5, attack_value=2, shop=self)
				weapon2.save()
				weapon3 = Weapon(name='Bloody Mary', description='A low-end sword', buy_value=65, sell_value=15, attack_value=5, shop=self)
				weapon3.save()
		elif self.location.area_difficulty_level == 2:
			weapon = Weapon(name='The Medium Cutter', description='A medium-end sword', buy_value=24, sell_value=15, shop=self)
			weapon.save()

	def generate_armor(self):
		if self.location.area_difficulty_level == 1:
			for x in range(0, 2):
				armor = Armor(name='The Protector', description='A basic set of armor, providing minimal protection', buy_value=14, sell_value=3, shop=self)
				armor.save()
				armor2 = Armor(name='Gladatorius', description='Basic armor that provides a small amount of protection', buy_value=20, sell_value=5, defense_value=3, shop=self)
				armor2.save()
		elif self.location.area_difficulty_level == 2:
			armor = Armor(name='The Medium Protector', description='A basic set of armor, providing minimal protection', buy_value=24, sell_value=15, shop=self)
			armor.save()


class Arena(models.Model):
	location = models.OneToOneField('Location', default=None, related_name='arena', blank=True, null=True)


	class Meta:
		app_label = 'arenafighter'

	def __unicode__(self):
		return 'An arena'

	def generate_enemy(self):
		strength_dict = {
			1: 'weak',
			2: 'medium',
			3: 'strong',
			4: 'very strong',
			5: 'exceptionally strong',
			6: 'powerful',
			7: 'exceptionally powerful',
    		8: 'ultimate',
			}
		strength = strength_dict[self.location.area_difficulty_level]
	#c    enemy = Enemy([x for x in enemy_strength_dict[strength]])
		enemy = Enemy(name=enemy_strength_dict[strength]['name'],
						xp_value=enemy_strength_dict[strength]['xp_value'],
						renown_value=enemy_strength_dict[strength]['renown_value'],
						hpmax=enemy_strength_dict[strength]['hpmax'],
						current_hp=enemy_strength_dict[strength]['hpmax'],
						base_attack=enemy_strength_dict[strength]['base_attack'],
						base_defense=enemy_strength_dict[strength]['base_defense'],
						gold=enemy_strength_dict[strength]['gold']
		)
		enemy.save()
	#    print 'name', enemy.name
	#    print 'xp', enemy.xp_value
	#    print 'renown', enemy.renown_value
	#    print 'hpmax', enemy.hpmax
	#    print 'current hp', enemy.current_hp
	#    print 'base attack', enemy.base_attack
	#    print 'base defense', enemy.base_defense
	#    print 'gold', enemy.gold
	#    enemy.delete()
		return enemy
