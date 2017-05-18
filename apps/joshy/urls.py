from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from apps.grophy import views

from django.contrib import admin
admin.autodiscover()

app_name = 'joshy'
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.joshy.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
