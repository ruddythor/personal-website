from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'arenafighter.views.home.home', name='home'),
    url(r'^store$', 'arenafighter.views.home.go_to_store', name='store'),
    url(r'^info/(\d+)/$', 'arenafighter.views.home.info', name='player_info'),
    url(r'^arena$', 'arenafighter.views.home.go_to_arena', name='battle'),
    url(r'^admin/', include(admin.site.urls)),
)
