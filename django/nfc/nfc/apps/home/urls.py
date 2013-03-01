from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('nfc.apps.home.views',
	url(r'^$','index_view',name='main_view'),
	url(r'^contact/$','contact_view',name='contact_view'),
	url(r'^error/$','my_custom_404_view',name="view_404"),
)