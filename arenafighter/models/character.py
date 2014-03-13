from django.db import models

from arenafighter.utils import dice
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon


class Character(models.Model):
    created_by = models.ForeignKey('Profile', null=False, related_name='created_characters')
    level = models.IntegerField(default=1)
    name = models.TextField(default="The Stranger")
    hpmax = models.IntegerField(default=dice.roll(15, 6))
    equipped_armor = models.ForeignKey('Armor', default=None, related_name='equipped_on', blank=True, null=True)
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
        for weapon in self.equipped_weapon.all():
            attack_value += weapon.attack_value
        attack = dice.roll(attack_value, 6)
        return attack

    def defense_value(self):
        defense_value = self.base_defense
        if self.equipped_armor:
            defense_value += self.equipped_armor.defense_value
        return defense_value

    def equip(self, item_type, item_id):
        if item_type == 'Weapon':
            weapon = Weapon.objects.get(id=item_id)
            weapon.equipped_on.add(self)
        elif item_type == 'InventoryItem':
            item = InventoryItem.objects.get(id=item_id)
            item.equipped_on = self
        elif item_type == 'Armor':
            armor = Armor.objects.get(id=item_id)
            self.equipped_armor = armor
        self.save()

    def unequip_weapon(self, weapon):
        weapon.equipped_on.remove(self.equipped)
        self.save()

    def Unequip_item(self, item):
        item.equipped_on = None#items.remove(self.equipped)
        self.save()

    def unequip_armor(self, armor):
        self.equipped_armor = None
        self.save()


    def purchase(self, item):
        if item.type == 'InventoryItem':
            self.inventory.items.add(item)
        elif item.type == 'Weapon':
            self.inventory.weapons.add(item)
        elif item.type == 'Armor':
            self.inventory.armor.add(item)
        self.gold -= item.buy_value
        self.save()

    def sell(self, item):
        self.inventory.remove(item)
        self.gold += item.sell_value
        self.save()

