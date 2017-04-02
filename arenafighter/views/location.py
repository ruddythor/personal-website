import collections
from django.shortcuts import render, redirect
from arenafighter.models.inventory import Inventory, Weapon, Armor, Potion
from arenafighter.models.character import Character
from arenafighter.forms import EquipArmorForm, EquipWeaponForm, PurchaseForm, SellForm, UnequipForm
from arenafighter.models.location import Location, Store, Arena



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

