from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'arenafighter.views.home.home', name='home'),
    url(r'^store$', 'arenafighter.views.store.shop', {'store_level': 1}, name='store'),
    url(r'^info/(\d+)/$', 'arenafighter.views.home.info', name='player_info'),
    url(r'^arena$', 'arenafighter.views.home.go_to_arena', name='arena'),

    url(r'^purchase/(?P<item_type>.+)/(?P<id>\d+)$', 'arenafighter.views.store.buy', name='buy'),

    url(r'^shop_item/(.+)$', 'arenafighter.views.store.item_detail', {'store': True}, name='shop_item'),
    url(r'^shop_weapon/(.+)$', 'arenafighter.views.store.weapon_detail', {'store': True}, name='shop_weapon'),
    url(r'^shop_armor/(.+)$', 'arenafighter.views.store.armor_detail', {'store': True}, name='shop_armor'),
    url(r'^item/(.+)$', 'arenafighter.views.store.item_detail', {'store': False}, name='item_info'),
    url(r'^weapon/(.+)$', 'arenafighter.views.store.weapon_detail', {'store': False}, name='weapon_info'),
    url(r'^armor/(.+)$', 'arenafighter.views.store.armor_detail', {'store': False}, name='armor_info'),

    url(r'^equip/(?P<item_type>.+)/(?P<item_id>\d+)$', 'arenafighter.views.home.equip', name='equip'),

    url(r'^fight', 'arenafighter.views.arena.fight', name='fight'),
    url(r'^play_as/(\d+)', 'arenafighter.views.home.play_as_character', name='play_as_character'),
    url(r'^delete/(\d+)', 'arenafighter.views.home.delete', name='delete'),
    url(r'^signup/', 'arenafighter.views.home.signup', name='signup'),
    url(r'^login/', 'arenafighter.views.home.log_in', name='log_in'),
    url(r'^logout/', 'arenafighter.views.home.log_out', name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
)
