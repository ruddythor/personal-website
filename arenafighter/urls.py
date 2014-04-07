from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'arenafighter.views.home.home', name='home'),
    url(r'^store$', 'arenafighter.views.store.shop', {'store_level': 1}, name='store'),
    url(r'^info/(\d+)/$', 'arenafighter.views.home.info', name='player_info'),
    url(r'^arena$', 'arenafighter.views.home.go_to_arena', name='arena'),

    url(r'^store/sell$', 'arenafighter.views.store.character_inventory', name='sell_detail'),


    url(r'^item/(\d+)$', 'arenafighter.views.store.item_detail', name='item_detail'),
    url(r'^store/item/(\d+)$', 'arenafighter.views.store.item_detail', {'store': True}, name='store_item_detail'),
    url(r'^store/sell/item/(\d+)$', 'arenafighter.views.store.item_detail', {'sell': True}, name='sell_item_detail'),

    url(r'^weapon/(\d+)$', 'arenafighter.views.store.weapon_detail', name='weapon_detail'),
    url(r'^store/weapon/(\d+)$', 'arenafighter.views.store.weapon_detail', {'store': True}, name='store_weapon_detail'),
    url(r'^store/sell/weapon/(\d+)$', 'arenafighter.views.store.weapon_detail', {'sell': True}, name='sell_weapon_detail'),

    url(r'^armor/(\d+)$', 'arenafighter.views.store.armor_detail', name='armor_detail'),
    url(r'^store/armor/(\d+)$', 'arenafighter.views.store.armor_detail', {'store': True}, name='store_armor_detail'),
    url(r'^store/sell/armor/(\d+)$', 'arenafighter.views.store.armor_detail', {'sell': True}, name='sell_armor_detail'),


    url(r'^fight', 'arenafighter.views.arena.fight', name='fight'),
    url(r'^fight/(?P<enemy_id>\d+)$', 'arenafighter.views.arena.fight', name='continued_fight'),


    url(r'^play_as/(\d+)', 'arenafighter.views.home.play_as_character', name='play_as_character'),
    url(r'^delete/(\d+)', 'arenafighter.views.home.delete', name='delete'),
    url(r'^signup/', 'arenafighter.views.home.signup', name='signup'),
    url(r'^login/', 'arenafighter.views.home.log_in', name='log_in'),
    url(r'^logout/', 'arenafighter.views.home.log_out', name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
)
