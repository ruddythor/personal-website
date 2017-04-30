import collections
from django.shortcuts import render, redirect
from apps.arenafighter.models.inventory import Inventory, Weapon, Armor, Potion
from apps.arenafighter.models.character import Character
from apps.arenafighter.forms import EquipArmorForm, EquipWeaponForm, PurchaseForm, SellForm, UnequipForm
from apps.arenafighter.models.location import Location, Store, Arena



def locations(request):
	locations = Location.objects.all()

	context = {#'potions': potions,
#				'num_potions': num_potions.values(),
#				'weapons': weapons,
#				'num_weapons': num_weapons.values(),
#				'armors': armor,
#				'num_armors': num_armor.values(),
#				'store': True,
				'locations': locations
				}
	return render(request, 'locations.html', context)


def area(request, id):
	area = Location.objects.get(id=id)
	character = Character.objects.get(id=request.user.profile.current_character_id)
	character.location = area
	character.save()
	context = {
		'area': area
	}
	return render(request, 'area.html', context)
