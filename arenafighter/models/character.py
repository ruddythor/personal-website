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
        if item_type == 'weapon':
            weapon = Weapon.objects.get(id=item_id)
            weapon.equipped_on.add(self)
        elif item_type == 'potion':
            item = Potion.objects.get(id=item_id)
            item.equipped_on = self
        elif item_type == 'armor':
            armor = Armor.objects.get(id=item_id)
            self.equipped_armor = armor
        self.save()

    def unequip_weapon(self, weapon):
        self.equipped_weapon.remove(weapon)
        self.save()

    def Unequip_item(self, item):
        item.equipped_on = None#items.remove(self.equipped)
        self.save()

    def unequip_armor(self, armor):
        self.equipped_armor = None
        self.save()


    def purchase(self, item):
        if item.type == 'potion':
            self.inventory.potion.add(item)
        elif item.type == 'weapon':
            self.inventory.weapon.add(item)
        elif item.type == 'armor':
            self.inventory.armor.add(item)
        self.gold -= item.buy_value
        self.save()

    def sell(self, item):
        if item.type == 'potion':
            self.inventory.potion.remove(item)
        elif item.type == 'weapon':
            self.inventory.weapons.remove(item)
            self.unequip_weapon(item)
        elif item.type == 'armor':
            self.inventory.armor.remove(item)
            self.unequip_armor(item)
        self.gold += item.sell_value
        self.save()

    @property
    def items(self):
        weapons = self.inventory.weapon.all()
        armor = self.inventory.armor.all()
        potions = self.inventory.potion.all()
        items = []
        items.extend(weapons)
        items.extend(armor)
        items.extend(potions)
        return items
