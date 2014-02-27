from django.db import models

from arenafighter.utils import dice
from arenafighter.models.equipment import Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.profile_model import Profile



class Player(models.Model):
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
        super(Player, self).__init__(*args, **kwargs)
        self.current_hp = self.hpmax

    def __unicode__(self):
        return self.name

    def attack(self):
        attack_value = self.base_attack
#        for item in self.equipped_items:
#            attack_value+=item.attack_value
        attack = dice.roll(attack_value, 6)
        return attack

    def defense_value(self):
        defense_value = self.base_defense
#        for item in self.equipped_items:
#            defense_value+=item.defense_value
        return defense_value

    def add(self, item):
        self.equipment.append(item)

    def drop(self, item):
        self.equipment.remove(item)

    def equip(self, item):
        weapons=0
        armors=0
        for x in self.equipped_items:
            if x.is_armor==True:
                armors+=1
            else:
                weapons+=1
        if len(self.equipped_items)>2:
            self.equipped_items.pop(0)
#            self.equipped_items.append(item)

        if armors<2 and item.is_armor==True:
            self.equipped_items.append(item)
        if weapons<2 and item.is_armor==False:
            self.equipped_items.append(item)

    def unequip(self, item):
        self.equipped_items.remove(item)

    def display_inventory(self):
        for item in self.equipment:
            print "\t", item
        return

    def display_equipped(self):
        print "\nThese are your equipped items:\n"
        for item in self.equipped_items:
            print "\t", item, "attack value: ", item.attack_value, "defense value: ", item.defense_value
#            print "\t", item
        return

    def buy(self, item):
        self.equipment.append(item)
        self.gold=self.gold-item.buy_value
        self.save()

    def sell(self, item):
        self.equipment.remove(item)
        self.gold+=item.sell_value
        self.save()
