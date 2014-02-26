from django import forms
from arenafighter.models.character import Player, Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.profile_model import Profile
from django.contrib.auth.models import User


class CreateCharacterForm(forms.ModelForm):
    name = forms.CharField(initial='Unknown')

    def save(self, name, user):
        # TODO fix this using signals, or something
        profile = Profile()
        profile.user = User.objects.get(id=user.id)
        profile.save()
        inventory = Inventory()
        new_character = Player(name=name)
        new_character.profile = profile
        new_character.save()
        new_character.inventory = inventory
        inventory.owner = new_character
        inventory.save()

    class Meta:
        model = Player
        fields = ('name',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
