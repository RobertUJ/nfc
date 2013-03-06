from django.contrib.admin import *
from django.contrib import admin
from nfc.apps.customers.models import ZipCode,Customer,Branch,PhotoGallery,phone_info
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.admin.filters import AllValuesFieldListFilter
from easy_maps.widgets import AddressWithMapWidget
from django import forms


class CustomerAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display        = ('name','slug',)
	search_fields		= ('name','slug',)

class PhotoGalleryAdmin(AdminImageMixin, admin.ModelAdmin):
	pass

class PhotoGalleryInline(AdminImageMixin, admin.StackedInline):
	model = PhotoGallery
	verbose_name = "Photo"
	max_num = 50
	extra = 0

class BranchAdmin(AdminImageMixin, admin.ModelAdmin):
	class form(forms.ModelForm):
		class Meta:
			widget={
				'dir_1': AddressWithMapWidget({'class':'vTextField'})
			}
			
	inlines = [PhotoGalleryInline,]
	prepopulated_fields = {"slug": ("name",)}
	list_display        = ('customer_name', 'name','Title','urltobranch','tag_id')
	list_filter         = ('ZipCode__zipcode','Customer__name','tag_id','featured',)
	search_fields		= ('name','tag_id','slug','Title','ZipCode__zipcode','Customer__name',)
	actions = ['duplicate_event']
	actions_on_top = True

	def customer_name(self,instance):
		return '%s' %(instance.Customer.name)
	customer_name.short_description = "Customer Name"

	def duplicate_event(modeladmin, request, queryset):
		con = 0
		for object in queryset:
			con += 1
			object.id = None
			object.name += " Copy %s --  %s" % (con,request.user)
			object.tag_id = "%s" % object.name
			object.save()
	duplicate_event.short_description = "Duplicate selected branch record"

	def urltobranch(self,instance):
		_url = '/%s/%s/%s/' % (instance.Customer.slug,instance.ZipCode.zipcode,instance.slug)
		return 	'<a target="_blank" href="%s">%s</a>' % (_url,_url)
	urltobranch.short_description = 'Url Shortcut'
	urltobranch.allow_tags = True



class phone_infoAdmin(admin.ModelAdmin):
	list_display        = ('zipcode','area','mobile',)
	search_fields		= ('zipcode','area','mobile',)
	list_filter         = ('zipcode','area','branch__Title')



admin.site.register(ZipCode)
# admin.site.register(PhotoGallery,PhotoGalleryAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(phone_info,phone_infoAdmin)
