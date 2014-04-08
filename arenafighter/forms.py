from django import forms



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


#TODO: look at changing these equip/purchase forms to model forms?
class EquipArmorForm(forms.Form):
    item_id = forms.IntegerField()

class EquipWeaponForm(forms.Form):
    item_id = forms.IntegerField()

class UnequipForm(forms.Form):
    item_id = forms.IntegerField()

class PurchaseForm(forms.Form):
    item_id = forms.IntegerField()

class SellForm(forms.Form):
    item_id = forms.IntegerField()

class GetItemForm(forms.Form):
    item_id = forms.IntegerField()

