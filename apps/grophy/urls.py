from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from apps.grophy import views

from django.contrib import admin
admin.autodiscover()

app_name = 'grophy'
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.grophy.views.home', name='home'),
    url(r'^/about', 'apps.grophy.views.about', name='about'),
    url(r'^blog/', 'apps.grophy.views.blog', name='blog'),
    url(r'^videos/', 'apps.grophy.views.videos', name='videos'),
    url(r'^resume/', 'apps.grophy.views.resume', name='resume'),
    url(r'^portfolio/', 'apps.grophy.views.portfolio', name='portfolio'),
#    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
