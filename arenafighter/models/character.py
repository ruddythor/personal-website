from django.db import models

from arenafighter.utils import dice
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.profile_model import Profile


class Character(models.Model):
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
        defense_value += self.equipped_armor.defense_value
        return defense_value


    def equip_weapon(self, weapon):
        weapon.equipped_weapon.add(self.equipped)
        self.save()

    def unequip_weapon(self, weapon):
        weapon.equipped_weapon.remove(self.equipped)
        self.save()

    def equip_armor(self, armor):
        self.equipped_armor = armor
        self.save()

    def Unequip_armor(self, armor):
        self.equipped_armor = None
        self.save()

    def equip_item(self, item):
        item.equipped_items.add(self.equipped)
        self.save()

    def Unequip_item(self, item):
        item.equipped_items.remove(self.equipped)
        self.save()

    def purchase(self, item):
        self.inventory.add(item)
        self.gold -= item.buy_value
        self.save()

    def sell(self, item):
        self.equipment.remove(item)
        self.gold += item.sell_value
        self.save()

#def character_equipped(character):
#    character = Character.objects.select_related('equipped').get(id=character.id)
#    equipment_dict = {'weapons': character.equipped.weapons, 'armor': character.equipped.armor, 'items': character.equipped.items}
#    return equipment_dict

#def character_inventory(character):
#    character = Character.objects.prefetch_related().get(id=character.id)
#    inventory_dict = {'weapons': character.inventory.weapons.all(), 'armor': character.inventory.armor.all(), 'items': character.inventory.items.all()}
#    return inventory_dict


#Character.equipped = property(lambda c: Equipped.objects.get_or_create(character=c)[0])
Character.inventory = property(lambda c: Inventory.objects.get_or_create(character=c)[0])

###c = Character.objects.get(id=1)
