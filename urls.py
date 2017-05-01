from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from basesite import views as basesite_views
from apps.arenafighter.views.home import home



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', basesite_views.home, name='sitehome'),
    url(r'^arena', include('apps.arenafighter.urls', namespace='arenafighter', app_name='arenafighter')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
