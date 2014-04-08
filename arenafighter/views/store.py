import collections
from django.shortcuts import render, redirect
from arenafighter.models.inventory import Inventory, Weapon, Armor, Potion
from arenafighter.models.character import Character
from arenafighter.forms import EquipArmorForm, EquipWeaponForm, PurchaseForm, SellForm, UnequipForm

# TODO: DE-uglify this view function
def shop(request, store_level):
    potions = Potion.objects.exclude(inventory__isnull=False)
    weapons = Weapon.objects.exclude(inventory__isnull=False)
    armor = Armor.objects.exclude(inventory__isnull=False)
    if not potions:
        generate_items(store_level)
    if not armor:
        generate_armor(store_level)
    if not weapons:
        generate_weapons(store_level)
    potions = Potion.objects.exclude(inventory__isnull=False)
    weapons = Weapon.objects.exclude(inventory__isnull=False)
    armor = Armor.objects.exclude(inventory__isnull=False)
    num_potions = dict(collections.Counter([item.name for item in potions]))
    num_weapons = dict(collections.Counter([item.name for item in weapons]))
    num_armor = dict(collections.Counter([item.name for item in armor]))
    context = {'potions': potions,
               'num_potions': num_potions.values(),
               'weapons': weapons,
               'num_weapons': num_weapons.values(),
               'armors': armor,
               'num_armors': num_armor.values(),
               'store': True,
               }
    return render(request, 'store.html', context)


def character_inventory(request):
    character = Character.objects.get(id=request.user.profile.current_character_id)
    items = dict(collections.Counter([item for item in character.items]))
    context = {'character': character,
               'items': items,
               'sell': True,
               }
    return render(request, 'character_sell_list.html', context)


# TODO: combine these *_detail views to be better
def potion_detail(request, id, store=False, sell=False):
    object = Potion.objects.get(id=id)
    if store:
        purchase_form = PurchaseForm()
    else:
        purchase_form = None
    if sell:
        sell_form = SellForm()
    else:
        sell_form = None
    context = {'item': object,
               'purchase_form': purchase_form,
               'sell_form': sell_form,
               }
    return render(request, 'item.html', context)


def armor_detail(request, id, store=False, sell=False):
    object = Armor.objects.get(id=id)
    equip_form = EquipArmorForm()
    unequip_form = UnequipForm()

    if store:
        purchase_form = PurchaseForm()
    else:
        purchase_form = None
    if sell:
        sell_form = SellForm()
    else:
        sell_form = None
    context = {'item': object,
               'equip_form': equip_form,
               'purchase_form': purchase_form,
               'sell_form': sell_form,
               'unequip_form': unequip_form,
               }
    return render(request, 'item.html', context)


def weapon_detail(request, id, store=False, sell=False):
    object = Weapon.objects.get(id=id)
    equip_form = EquipWeaponForm()
    unequip_form = UnequipForm()
    if store:
        purchase_form = PurchaseForm()
    else:
        purchase_form = None
    if sell:
        sell_form = SellForm()
    else:
        sell_form = None
    context = {'item': object,
               'equip_form': equip_form,
               'purchase_form': purchase_form,
               'sell_form': sell_form,
               'unequip_form': unequip_form,
               }
    return render(request, 'item.html', context)


def purchase_potion(request, item_id):
    if request.POST:
        item = Potion.objects.get(id=item_id)
        request.user.profile.current_character.purchase(item)
    return redirect('store')


def purchase_weapon(request, item_id):
    if request.POST:
        item = Weapon.objects.get(id=item_id)
        request.user.profile.current_character.purchase(item)
    return redirect('store')


def purchase_armor(request, item_id):
    if request.POST:
        item = Armor.objects.get(id=item_id)
        request.user.profile.current_character.purchase(item)
    return redirect('store')

def sell_potion(request, item_id):
    if request.POST:
        item = Potion.objects.get(id=item_id)
        request.user.profile.current_character.sell(item)
    return redirect('store')


def sell_weapon(request, item_id):
    if request.POST:
        item = Weapon.objects.get(id=item_id)
        request.user.profile.current_character.sell(item)
    return redirect('store')


def sell_armor(request, item_id):
    if request.POST:
        item = Armor.objects.get(id=item_id)
        request.user.profile.current_character.sell(item)
    return redirect('store')



def generate_items(store_level):
    if store_level == 1:
        for x in range(0, 10):
            potion = Potion(name='Health Potion', description='potion', buy_value=10, sell_value=2)
            potion.save()

def generate_weapons(store_level):
    if store_level == 1:
        for x in range(0, 2):
            weapon = Weapon(name='Cutter', description='A basic sword', buy_value=12, sell_value=3, attack_value=1)
            weapon.save()
            weapon2 = Weapon(name='Kamikaze', description='A low-end sword', buy_value=20, sell_value=5, attack_value=2)
            weapon2.save()
            weapon3 = Weapon(name='Bloody Mary', description='A low-end sword', buy_value=65, sell_value=15, attack_value=5)
            weapon3.save()


def generate_armor(store_level):
    if store_level == 1:
        for x in range(0, 2):
            armor = Armor(name='The Protector', description='A basic set of armor, providing minimal protection', buy_value=14, sell_value=3)
            armor.save()
            armor2 = Armor(name='Gladatorius', description='Basic armor that provides a small amount of protection', buy_value=20, sell_value=5, defense_value=3)
            armor2.save()
