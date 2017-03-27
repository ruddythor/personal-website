'''
Created on Oct 1, 2012

@author: josh
'''
from arenafighter.utils import dice
from django.db import models


class Enemy(models.Model):
    name = models.TextField(default="An Enemy!")
    xp_value = models.IntegerField(default=5)
    renown_value = models.IntegerField(default=10)
    hpmax = models.IntegerField()
    current_hp = models.IntegerField(default=0)
    base_attack = models.IntegerField(default=4)
    base_defense = models.IntegerField(default=5)
    gold = models.IntegerField()
    dead = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    class Meta:
        app_label = 'arenafighter'

    def __init__(self, *args, **kwargs):
        super(Enemy, self).__init__(*args, **kwargs)
        #### THIS IS A BUG NOW, I THINK BECAUSE OF CHANGES TO __INIT__(?)
        self.hpmax = dice.roll(15, 6)
        self.gold = dice.roll(5, 6)

    def attack(self, enemy):
        attack_value = self.base_attack
#        for item in self.equipped_items:
#            if hasattr(item, 'attack_value'):
#                attack_value += item.attack_value
        attack = dice.roll(attack_value, 6)
        damage = attack - enemy.defense_value
        if damage <= 0:
            return
        if damage > 0:
            enemy.current_hp -= damage
            enemy.save()
            return

    @property
    def defense_value(self):
        defense_value=self.base_defense
#        for item in self.equipped_items:
#            defense_value+=item.defense_value
        return int(defense_value)

    def equip(self, item):
        pass
#        weapons=0
#        armors=0
#        for x in self.equipped_items:
#            if x.is_armor==True:
#                armors+=1
#            else:
#                weapons+=1
#        if len(self.equipped_items)>2:
#            self.equipped_items.pop(0)#

#        if self.equipment.index(item):
#            if armors<=0 and item.is_armor==True:
#                self.equipped_items.append(item)
#            elif weapons<=1 and item.is_armor==False:
#                self.equipped_items.append(item)
#        else:
#            print "You have too many of that type of item equipped. Try again."#

    def unequip(self, item):
#        self.equipped_items.remove(item)
        pass



    def display_equipped(self):
        pass
#        print "These are your equipped items"
#        for item in self.equipped_items:
#            print "\t", item
#        return

    def initiative_roll(self):
        roll = dice.roll(1, 21)
        return roll

enemy_strength_dict = {
    'weak': {'name': 'An Enemy!',
             'xp_value': 5,
             'renown_value': 7,
             'hpmax': dice.roll(13, 5),
             'current_hp': 0,
             'base_attack': 4,
             'base_defense': 5,
             'gold': dice.roll(5, 7)
             },
    'medium': {'name': 'An Enemy!',
               'xp_value': 15,
               'renown_value': 14,
               'hpmax': dice.roll(17, 5),
               'current_hp': 0,
               'base_attack': 8,
               'base_defense': 8,
               'gold': dice.roll(9, 7)
                },
    'strong': {'name': 'An Enemy!',
               'xp_value': 45,
               'renown_value': 21,
               'hpmax': dice.roll(25, 5),
               'current_hp': 0,
               'base_attack': 15,
               'base_defense': 15,
               'gold': dice.roll(15, 5)
                },
    'very strong': {'name': 'An Enemy!', 'xp_value': 65, 'renown_value': 28, 'hpmax': dice.roll(35, 5), 'current_hp': 0, 'base_attack': 25, 'base_defense': 25, 'gold': dice.roll(20, 5)},
    'exceptionally strong': {'name': 'An Enemy!', 'xp_value': 95, 'renown_value': 35, 'hpmax': dice.roll(50, 5), 'current_hp': 0, 'base_attack': 40, 'base_defense': 45, 'gold': dice.roll(30, 5)},
    'powerful': {'name': 'An Enemy!', 'xp_value': 145, 'renown_value': 42, 'hpmax': dice.roll(65, 4), 'current_hp': 0, 'base_attack': 75, 'base_defense': 75, 'gold': dice.roll(45, 4)},
    'exceptionally powerful': {'name': 'An Enemy!', 'xp_value': 180, 'renown_value': 49, 'hpmax': dice.roll(75, 4), 'current_hp': 0, 'base_attack': 100, 'base_defense': 100, 'gold': dice.roll(65, 4)},
    'ultimate': {'name': 'An Enemy!', 'xp_value': 250, 'renown_value': 200, 'hpmax': dice.roll(100, 4), 'current_hp': 0, 'base_attack': 200, 'base_defense': 150, 'gold': dice.roll(80, 5)},
}

def generate_enemy(strength):
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