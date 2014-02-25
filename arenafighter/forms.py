from django import forms
from arenafighter.models.character import Player, Inventory, InventoryItem, Armor, Weapon


class CreateCharacterForm(forms.Form):
    name = forms.CharField(initial='Unknown')

    def save(self, name):
        # TODO fix this using signals, or something
        sword = Weapon(name='sword')
        inventory = Inventory()
        new_character = Player(name=name)
        new_character.save()
        new_character.inventory = inventory
        sword.inventory = inventory
        inventory.save()
        inventory.owner = new_character
        inventory.weapons.add(sword)
        sword.save()





