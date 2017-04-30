from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.personal.views.home.home', name='sitehome'),
    url(r'^arena$', 'apps.arenafighter.views.home.home', name='home'),
    url(r'^arena/store$', 'apps.arenafighter.views.store.shop', {'store_level': 1}, name='store'),
    url(r'^arena/info/(\d+)/$', 'apps.arenafighter.views.home.info', name='player_info'),
    url(r'^arena/arena$', 'apps.arenafighter.views.home.go_to_arena', name='arena'),

    url(r'^arena/store/sell$', 'apps.arenafighter.views.store.character_inventory', name='sell_detail'),

    url(r'^arena/equip/weapon/(\d+)$', 'apps.arenafighter.views.home.equip_weapon', name='equip_weapon'),
    url(r'^arena/equip/armor/(\d+)$', 'apps.arenafighter.views.home.equip_armor', name='equip_armor'),
    url(r'^arena/unequip/weapon/(\d+)$', 'apps.arenafighter.views.home.unequip_weapon', name='unequip_weapon'),
    url(r'^arena/unequip/armor/(\d+)$', 'apps.arenafighter.views.home.unequip_armor', name='unequip_armor'),


    url(r'^arena/item/(\d+)$', 'apps.arenafighter.views.store.potion_detail', name='potion_detail'),
    url(r'^arena/store/item/(\d+)$', 'apps.arenafighter.views.store.potion_detail', {'store': True}, name='store_potion_detail'),
    url(r'^arena/store/sell/item/(\d+)$', 'apps.arenafighter.views.store.sell_potion', name='sell_potion'),
    url(r'^arena/store/buy/item/(\d+)$', 'apps.arenafighter.views.store.purchase_potion', name='purchase_potion'),

    url(r'^arena/weapon/(\d+)$', 'apps.arenafighter.views.store.weapon_detail', name='weapon_detail'),
    url(r'^arena/store/weapon/(\d+)$', 'apps.arenafighter.views.store.weapon_detail', {'store': True}, name='store_weapon_detail'),
    url(r'^arena/store/sell/weapon/(\d+)$', 'apps.arenafighter.views.store.sell_weapon', name='sell_weapon'),
    url(r'^arena/store/buy/weapon/(\d+)$', 'apps.arenafighter.views.store.purchase_weapon', name='purchase_weapon'),

    url(r'^arena/armor/(\d+)$', 'apps.arenafighter.views.store.armor_detail', name='armor_detail'),
    url(r'^arena/store/armor/(\d+)$', 'apps.arenafighter.views.store.armor_detail', {'store': True}, name='store_armor_detail'),
    url(r'^arena/store/sell/armor/(\d+)$', 'apps.arenafighter.views.store.sell_armor', name='sell_armor'),
    url(r'^arena/store/buy/armor/(\d+)$', 'apps.arenafighter.views.store.purchase_armor', name='purchase_armor'),


    url(r'^arena/fight', 'apps.arenafighter.views.arena.fight', name='fight'),
    url(r'^arena/attack$', 'apps.arenafighter.views.arena.attack', name='attack'),

    url(r'^arena/use-potion$', 'apps.arenafighter.views.arena.use_potion', name='use_potion'),

    url(r'^arena/locations', 'apps.arenafighter.views.location.locations', name='locations'),
    url(r'^arena/area/(\d+)', 'apps.arenafighter.views.location.area', name='area_detail'),

    url(r'^arena/play_as/(\d+)', 'apps.arenafighter.views.home.play_as_character', name='play_as_character'),
    url(r'^arena/delete/(\d+)', 'apps.arenafighter.views.home.delete', name='delete'),
    url(r'^arena/signup/', 'apps.arenafighter.views.home.signup', name='signup'),
    url(r'^arena/login/', 'apps.arenafighter.views.home.log_in', name='log_in'),
    url(r'^arena/logout/', 'apps.arenafighter.views.home.log_out', name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
