from django.contrib import admin
from arenafighter.models.character import Character
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon, Potion
from arenafighter.models.enemy import Enemy
from arenafighter.models.profile_model import Profile
from arenafighter.models.location import Location, Store, Arena


class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)


class PotionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Potion, PotionAdmin)


#class InventoryAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Inventory, InventoryAdmin)


#class InventoryItemAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(InventoryItem, InventoryItemAdmin)


class ArmorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Armor, ArmorAdmin)


class WeaponAdmin(admin.ModelAdmin):
    pass
admin.site.register(Weapon, WeaponAdmin)


class EnemyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Enemy, EnemyAdmin)


class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)


class LocationAdmin(admin.ModelAdmin):
	pass
admin.site.register(Location, LocationAdmin)


class StoreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Store, StoreAdmin)

class ArenaAdmin(admin.ModelAdmin):
	pass
admin.site.register(Arena, ArenaAdmin)




#class EquippedAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Equipped, EquippedAdmin)


