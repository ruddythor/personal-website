from django.db import models


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


class Armor(InventoryItem):
    defense_value = models.IntegerField(default=2)
    type = models.TextField(default='armor', editable=False)
    shop = models.ForeignKey('Store', default=None, related_name='armors', blank=True, null=True)


    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name

class Weapon(InventoryItem):
    attack_value = models.IntegerField(default=2)
    type = models.TextField(default='weapon', editable=False)
    shop = models.ForeignKey('Store', default=None, related_name='weapons', blank=True, null=True)


    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name

class Potion(InventoryItem):
    heal_percent = models.IntegerField(default=20)
    type = models.TextField(default='potion', editable=False)
    shop = models.ForeignKey('Store', default=None, related_name='potions', blank=True, null=True)


    class Meta:
        app_label = 'arenafighter'

    def __unicode__(self):
        return self.name

