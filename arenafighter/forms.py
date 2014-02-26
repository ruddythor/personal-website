from django import forms
from arenafighter.models.character import Player, Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.profile_model import Profile
from django.contrib.auth.models import User



class CreateCharacterForm(forms.Form):
    name = forms.CharField(initial='Unknown')


#    class Meta:
#        model = Player
#        fields = ('name',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
