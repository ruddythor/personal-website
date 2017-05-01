from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from apps.arenafighter import views

from django.contrib import admin
admin.autodiscover()

app_name = 'arenafighter'
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.arenafighter.views.home.home', name='home'),
    url(r'^store$', 'apps.arenafighter.views.store.shop', {'store_level': 1}, name='store'),
    url(r'^info/(\d+)/$', 'apps.arenafighter.views.home.info', name='player_info'),
    url(r'^arena$', 'apps.arenafighter.views.home.go_to_arena', name='arena'),

    url(r'^store/sell$', 'apps.arenafighter.views.store.character_inventory', name='sell_detail'),

    url(r'^equip/weapon/(\d+)$', 'apps.arenafighter.views.home.equip_weapon', name='equip_weapon'),
    url(r'^equip/armor/(\d+)$', 'apps.arenafighter.views.home.equip_armor', name='equip_armor'),
    url(r'^unequip/weapon/(\d+)$', 'apps.arenafighter.views.home.unequip_weapon', name='unequip_weapon'),
    url(r'^unequip/armor/(\d+)$', 'apps.arenafighter.views.home.unequip_armor', name='unequip_armor'),


    url(r'^item/(\d+)$', 'apps.arenafighter.views.store.potion_detail', name='potion_detail'),
    url(r'^store/item/(\d+)$', 'apps.arenafighter.views.store.potion_detail', {'store': True}, name='store_potion_detail'),
    url(r'^store/sell/item/(\d+)$', 'apps.arenafighter.views.store.sell_potion', name='sell_potion'),
    url(r'^store/buy/item/(\d+)$', 'apps.arenafighter.views.store.purchase_potion', name='purchase_potion'),

    url(r'^weapon/(\d+)$', 'apps.arenafighter.views.store.weapon_detail', name='weapon_detail'),
    url(r'^store/weapon/(\d+)$', 'apps.arenafighter.views.store.weapon_detail', {'store': True}, name='store_weapon_detail'),
    url(r'^store/sell/weapon/(\d+)$', 'apps.arenafighter.views.store.sell_weapon', name='sell_weapon'),
    url(r'^store/buy/weapon/(\d+)$', 'apps.arenafighter.views.store.purchase_weapon', name='purchase_weapon'),

    url(r'^armor/(\d+)$', 'apps.arenafighter.views.store.armor_detail', name='armor_detail'),
    url(r'^store/armor/(\d+)$', 'apps.arenafighter.views.store.armor_detail', {'store': True}, name='store_armor_detail'),
    url(r'^store/sell/armor/(\d+)$', 'apps.arenafighter.views.store.sell_armor', name='sell_armor'),
    url(r'^store/buy/armor/(\d+)$', 'apps.arenafighter.views.store.purchase_armor', name='purchase_armor'),


    url(r'^fight', 'apps.arenafighter.views.arena.fight', name='fight'),
    url(r'^attack$', 'apps.arenafighter.views.arena.attack', name='attack'),

    url(r'^use-potion$', 'apps.arenafighter.views.arena.use_potion', name='use_potion'),

    url(r'^locations', 'apps.arenafighter.views.location.locations', name='locations'),
    url(r'^area/(\d+)', 'apps.arenafighter.views.location.area', name='area_detail'),

    url(r'^play_as/(\d+)', 'apps.arenafighter.views.home.play_as_character', name='play_as_character'),
    url(r'^delete/(\d+)', 'apps.arenafighter.views.home.delete', name='delete'),
    url(r'^signup/', 'apps.arenafighter.views.home.signup', name='signup'),
    url(r'^login/', 'apps.arenafighter.views.home.log_in', name='log_in'),
    url(r'^logout/', 'apps.arenafighter.views.home.log_out', name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
