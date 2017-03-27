'''
Created on Oct 1, 2012

@author: josh
'''
from arenafighter.utils import dice
from django.db import models
from arenafighter.models.enemy import Enemy, generate_enemy

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
    		4: 'very strong'
    	}
    	strength = strength_dict[self.area_difficulty_level]
    	enemy = generate_enemy(strength)
    	return enemy


