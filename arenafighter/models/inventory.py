from django.db import models
import random


class Inventory(models.Model):
    slots = models.IntegerField(default=10)
    slots_filled = models.IntegerField(default=0)
    slots_empty = models.IntegerField(default=10)
    character = models.OneToOneField('Character', default=None, related_name='inventory', blank=False, null=False)

    class Meta:
        verbose_name_plural = "inventories"
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.character.name


class InventoryItem(models.Model):
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    buy_value = models.IntegerField(default=0)
    sell_value = models.IntegerField(default=0)
    slots_required = models.IntegerField(default=1)
    inventory = models.ForeignKey('Inventory', default=None, related_name='%(class)s', blank=True, null=True)
    equipped = models.BooleanField(default=False)

    class Meta:
        abstract = True
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name

class SpecialWeaponItemProperty(models.Model):
    description = models.TextField(default='')

    class Meta:
        app_label = 'arenafighter'

class SpecialArmorItemProperty(models.Model):
    description = models.TextField(default='')

    class Meta:
        app_label = 'arenafighter'


class Armor(InventoryItem):
    defense_value = models.IntegerField(default=2)
    special_property = models.ForeignKey('SpecialArmorItemProperty', default=None, related_name='armors', blank=True, null=True)
    type = models.TextField(default='armor', editable=False)

    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name

class Weapon(InventoryItem):
    attack_value = models.IntegerField(default=2)
    special_property = models.ForeignKey('SpecialWeaponItemProperty', default=None, related_name='weapons', blank=True, null=True)
    type = models.TextField(default='weapon', editable=False)

    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name


    def get_damage(self):
        adjustment_min = .9
        adjustment_max = 1.1
        wildcard_adjustment = random.uniform(adjustment_min, adjustment_max)
        damage = self.attack_value ** 1.5
        damage = damage * wildcard_adjustment

        return damage


    def get_damage_roll(self):
        multiplier = None
        min_random = None
        max_random = None
        if self.attack_value in range(0, 30):
            multiplier = 1
            min_random = 3.0
            max_random = 5.0
        elif self.attack_value in range(31, 70):
            multiplier = 1.15
            min_random = 4.0
            max_random = 6.0
        elif self.attack_value in range(71, 100):
            multiplier = 1.3
            min_random = 5.0
            max_random = 8.0
        else:
            multiplier = 1.5
            min_random = 7.0
            max_random = 10.0

        base_damage = random.uniform(min_random, max_random)
        damage = round(base_damage * self.attack_value * multiplier, 1)
        return damage


    def tally_damage_stats(self):
        value_dict = {}
        vals = []
        for x in range(0, 1000):
            vals.append(self.get_damage_roll())
        for val in vals:
            value = str(val)
            if value in value_dict.keys():
                value_dict[value] += 1
            else:
                value_dict[value] = 1
        return value_dict


#w = Weapon.objects.get(id=7)
#results = w.tally_damage_stats()
class Potion(InventoryItem):
    heal_percent = models.IntegerField(default=20)
    type = models.TextField(default='potion', editable=False)

    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name

