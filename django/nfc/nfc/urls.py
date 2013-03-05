from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'nfc.apps.home.views.my_custom_404_view'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nfc.views.home', name='home'),
    # url(r'^nfc/', include('nfc.foo.urls')),

    #import urls.py's apps
     url(r'^',include('nfc.apps.home.urls')),
     url(r'^',include('nfc.apps.customers.urls')),
     url('^pages/',include('django.contrib.flatpages.urls')),	
     

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)
