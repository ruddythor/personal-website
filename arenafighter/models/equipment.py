from django.db import models

class Equipment(models.Model):
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    buy_value = models.IntegerField(default=0)
    sell_value = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class Armor(Equipment):
    defense_value = models.IntegerField(default=2)
    is_armor = models.BooleanField(default=True)

class Weapon(Equipment):
    attack_value = models.IntegerField(default=2)