from django import forms
from arenafighter.models.character import Character, Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.profile_model import Profile
from django.contrib.auth.models import User



class CreateCharacterForm(forms.Form):
    name = forms.CharField(initial='Unknown')


#    class Meta:
#        model = Character
#        fields = ('name',)


class ContinueFightForm(forms.Form):
    keep_fighting = forms.BooleanField(required=True)
    enemy_id = forms.IntegerField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class EquipArmorForm(forms.Form):
    item_id = forms.IntegerField()

class EquipWeaponForm(forms.Form):
    item_id = forms.IntegerField()

