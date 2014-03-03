from django.db import models

from arenafighter.utils import dice
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.profile_model import Profile


class Equipped(models.Model):
    character = models.OneToOneField('Character', default=None, related_name='equipped')
    items = models.ForeignKey('InventoryItem', default=None, related_name='equipped_on', null=True)
    weapons = models.ForeignKey('Weapon', default=None, null=True, related_name='equipped_on')
    armor = models.ForeignKey('Armor', default=None, null=True, related_name='equipped_on')

    class Meta:
        verbose_name_plural = "Equipped Objects"
        app_label = 'arenafighter'



class Character(models.Model):
    level = models.IntegerField(default=1)
    name = models.TextField(default="The Stranger")
    hpmax = models.IntegerField(default=dice.roll(15, 6))
    current_hp = models.IntegerField()
    base_attack = models.IntegerField(default=2)
    base_defense = models.IntegerField(default=3)
    gold = models.IntegerField(default=50)
    xp = models.IntegerField(default=0)
    renown = models.IntegerField(default=0)
    next_levelup = models.IntegerField(default=100)
    num_armor = models.IntegerField(default=0)
    fights_won = models.IntegerField(default=0)
    fights_lost = models.IntegerField(default=0)

    class Meta:
        app_label = 'arenafighter'

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self.current_hp = self.hpmax

    def __unicode__(self):
        return self.name

    def attack(self):
        attack_value = self.base_attack
#        for weapon in self.equipped.weapons:
        attack_value += self.equipped.weapons.attack_value
        attack = dice.roll(attack_value, 6)
        return attack

    def defense_value(self):
        defense_value = self.base_defense
        defense_value += self.equipped.armor.defense_value
        return defense_value


    def equip_weapon(self, weapon):
        weapon.equipped_on.add(self.equipped)
        self.save()

    def unequip_weapon(self, weapon):
        weapon.equipped_on.remove(self.equipped)
        self.save()

    def equip_armor(self, armor):
        armor.equipped_on.add(self.equipped)
        self.save()

    def Unequip_armor(self, armor):
        armor.equipped_on.remove(self.equipped)
        self.save()

    def equip_item(self, item):
        item.equipped_on.add(self.equipped)
        self.save()

    def Unequip_item(self, item):
        item.equipped_on.remove(self.equipped)
        self.save()

    def all_equipped(self):
        equipment_dict = {'weapons': self.equipped.weapons, 'armor': self.equipped.armor, 'items': self.equipped.items}
        return equipment_dict

    def all_inventory(self):
        inventory_dict = {'weapons': self.inventory.weapons.all(), 'armor': self.inventory.armor.all(), 'items': self.inventory.items.all()}
        return inventory_dict

    def purchase(self, item):
        self.inventory.add(item)
        self.gold -= item.buy_value
        self.save()

    def sell(self, item):
        self.equipment.remove(item)
        self.gold += item.sell_value
        self.save()


Character.equipped = property(lambda c: Equipped.objects.get_or_create(character=c)[0])
Character.inventory = property(lambda c: Inventory.objects.get_or_create(character=c)[0])

###c = Character.objects.get(id=1)
