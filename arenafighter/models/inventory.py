from django.db import models


class Inventory(models.Model):
    slots = models.IntegerField(default=10)
    slots_filled = models.IntegerField(default=0)
    slots_empty = models.IntegerField(default=10)
    character = models.OneToOneField('Character', default=None, related_name='inventory', blank=True, null=True)

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
    equipped_on = models.ManyToManyField('Character', default=None, related_name='equipped_items', blank=True, null=True)
    inventory = models.ManyToManyField('Inventory', default=None, related_name='items', blank=True, null=True)
    type = models.TextField(default='InventoryItem', editable=False)

    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name


class Armor(models.Model):
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    buy_value = models.IntegerField(default=0)
    sell_value = models.IntegerField(default=0)
    defense_value = models.IntegerField(default=2)
    slots_required = models.IntegerField(default=2)
    inventory = models.ManyToManyField('Inventory', default=None, related_name='armor', blank=True, null=True)
    type = models.TextField(default='Armor', editable=False)

    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name

class Weapon(models.Model):
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    buy_value = models.IntegerField(default=0)
    sell_value = models.IntegerField(default=0)
    attack_value = models.IntegerField(default=2)
    equipped_on = models.ManyToManyField('Character', default=None, related_name='equipped_weapon', blank=True, null=True)
    slots_required = models.IntegerField(default=1)
    inventory = models.ManyToManyField('Inventory', default=None, related_name='weapons', blank=True, null=True)
    type = models.TextField(default='Weapon', editable=False)

    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name