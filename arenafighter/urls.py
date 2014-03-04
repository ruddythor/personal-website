from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'arenafighter.views.home.home', name='home'),
    url(r'^store$', 'arenafighter.views.store.shop', {'store_level': 1}, name='store'),
    url(r'^info/(\d+)/$', 'arenafighter.views.home.info', name='player_info'),
    url(r'^arena$', 'arenafighter.views.home.go_to_arena', name='arena'),


    url(r'^armor/purchase/(\d+)$', 'arenafighter.views.store.buy_armor', name='buy_armor'),
    url(r'^weapon/purchase/(\d+)$', 'arenafighter.views.store.buy_weapon', name='buy_weapon'),
    url(r'^item/purchase/(\d+)$', 'arenafighter.views.store.buy_item', name='buy_item'),
    url(r'^item/(\d+)$', 'arenafighter.views.store.item_detail', name='item_info'),
    url(r'^weapon/(\d+)$', 'arenafighter.views.store.weapon_detail', name='weapon_info'),
    url(r'^armor/(\d+)$', 'arenafighter.views.store.armor_detail', name='armor_info'),

    url(r'^fight', 'arenafighter.views.arena.fight', name='fight'),
    url(r'^play_as/(\d+)', 'arenafighter.views.home.play_as_character', name='play_as_character'),
    url(r'^delete/(\d+)', 'arenafighter.views.home.delete', name='delete'),
    url(r'^signup/', 'arenafighter.views.home.signup', name='signup'),
    url(r'^login/', 'arenafighter.views.home.log_in', name='log_in'),
    url(r'^logout/', 'arenafighter.views.home.log_out', name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
)
