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
    url(r'^/about', 'apps.grophy.views.about', name='about_grophy'),
    url(r'^blog/', 'apps.grophy.views.blog', name='blog'),
    url(r'^video-compositing', 'apps.grophy.views.video_compositing', name='video_compositing'),
    url(r'^photography', 'apps.grophy.views.photography', name='photography'),
    url(r'^short-film', 'apps.grophy.views.short_film', name='short_film'),
    url(r'^illustration', 'apps.grophy.views.illustration', name='illustration'),
    url(r'^logo-design', 'apps.grophy.views.logo_design', name='logo_design'),
    url(r'^character-design', 'apps.grophy.views.character_design', name='character_design'),
    url(r'^user-experience', 'apps.grophy.views.user_experience', name='user_experience'),
    url(r'^painting', 'apps.grophy.views.painting', name='painting'),
    url(r'^drawing', 'apps.grophy.views.drawing', name='drawing'),
    url(r'^2d', 'apps.grophy.views.two_d', name='two_d'),
    url(r'^3d', 'apps.grophy.views.three_d', name='three_d'),
#    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
