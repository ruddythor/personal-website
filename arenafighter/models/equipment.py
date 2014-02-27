from django.db import models


class Inventory(models.Model):
    slots = models.IntegerField(default=10)
    slots_filled = models.IntegerField(default=0)
    slots_empty = models.IntegerField(default=10)
    owner = models.OneToOneField('Player', default=None, related_name='inventory', blank=True, null=True)

    class Meta:
        app_label = 'arenafighter'



class InventoryItem(models.Model):
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    buy_value = models.IntegerField(default=0)
    sell_value = models.IntegerField(default=0)
    slots_required = models.IntegerField(default=1)
    inventory = models.ManyToManyField('Inventory', default=None, related_name='items', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    class Meta:
        app_label = 'arenafighter'


class Armor(models.Model):
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    buy_value = models.IntegerField(default=0)
    sell_value = models.IntegerField(default=0)
    defense_value = models.IntegerField(default=2)
    is_armor = models.BooleanField(default=True)
    equipped = models.BooleanField(default=False)
    slots_required = models.IntegerField(default=2)
    inventory = models.ManyToManyField('Inventory', default=None, related_name='armor', blank=True, null=True)

    class Meta:
        app_label = 'arenafighter'


class Weapon(models.Model):
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    buy_value = models.IntegerField(default=0)
    sell_value = models.IntegerField(default=0)
    attack_value = models.IntegerField(default=2)
    equipped = models.BooleanField(default=False)
    slots_required = models.IntegerField(default=1)
    inventory = models.ManyToManyField('Inventory', default=None, related_name='weapons', blank=True, null=True)

    class Meta:
        app_label = 'arenafighter'
