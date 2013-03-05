from django.db import models
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField

class Customer(models.Model):
	name 		=  models.CharField(max_length=255,null=False,blank=False,unique=True,verbose_name=u'Client Name')
	slug		=  models.SlugField(max_length=255,null=True,blank=True,unique=True)
	active		=  models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.name)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Customer,self).save(*args,**kwargs)

class ZipCode(models.Model):
	zipcode 		= models.PositiveIntegerField(null=False,blank=False,unique=True)
	def __unicode__(self):
		return str(self.zipcode)

class Branch(models.Model):
	tag_id 			= models.CharField(max_length=255,blank=False,null=False,unique=False)
	Customer 		= models.ForeignKey(Customer)
	ZipCode 		= models.ForeignKey(ZipCode)
	adult_required  = models.BooleanField(default=False,verbose_name=u'Adult Required')
	age_required	= models.IntegerField(blank=True,null=True)
	name 			= models.CharField(max_length=255,null=False,blank=False,unique=True)
	slug 			= models.SlugField(max_length=255,null=True,blank=True,unique=True)
	Title 			= models.CharField(max_length=255)
	Logo  			= models.ImageField(upload_to='branch/logos')
	Video			= models.TextField(help_text='After making your selection in youtube, copy and paste the embed code of the video selected.',blank=True,null=True)
	Coupon			= models.ImageField(upload_to='branch/cupon',blank=True,null=True)
	Desc_featured	= models.TextField(blank=True,null=True,verbose_name=u'Description featured section')
	Description		= models.TextField(blank=True,null=True,verbose_name=u'Description mini web site')
	Contact			= models.TextField(blank=True,null=True)
	facebook		= models.URLField(max_length=200,verify_exists=True,null=True,blank=True)
	gmail			= models.URLField(max_length=200,verify_exists=True,null=True,blank=True)
	twitter			= models.URLField(max_length=200,verify_exists=True,null=True,blank=True)
	mail 			= models.EmailField(max_length=255,null=True,blank=True)
	website			= models.URLField(max_length=200,verify_exists=True,null=True,blank=True)
	featured 		= models.BooleanField(default=False)
	background_img  = models.ImageField(upload_to='branch/background',null=True,blank=True)
	id_body			= models.CharField(max_length=20,null=True,blank=True)
	show_dir		= models.BooleanField(default=False)
	dir_1 			= models.CharField(max_length=255,null=True,blank=True)
	dir_2 			= models.CharField(max_length=255,null=True,blank=True)
	cd 	 			= models.CharField(max_length=255,null=True,blank=True)
	state 			= models.CharField(max_length=255,null=True,blank=True)
	zip_code		= models.CharField(max_length=255,null=True,blank=True)
	info_cupon		= models.TextField(blank=True,null=True)
	image_cupon		= models.ImageField(upload_to='branch/cupon/info',blank=True,null=True)
	text_cupon      = models.CharField(null=True,blank=True,default="Get a Coupon")
	latitude		= models.CharField(max_length=255,null=True,blank=True)
	longitude		= models.CharField(max_length=255,null=True,blank=True)
	
	def __unicode__(self):
		return str(self.Title)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Branch,self).save(*args,**kwargs)

class PhotoGallery(models.Model):
	Branch 			= models.ForeignKey(Branch)
	Image_Title	    = models.CharField(max_length=255,null=True,blank=True,unique=False)
	Image 			= models.ImageField(upload_to='branch/galery')
	def __unicode__(self):
		return str(self.Image_Title)

class phone_info(models.Model):
	branch 	= models.ForeignKey(Branch)
	zipcode = models.IntegerField(max_length=5)
	area 	= models.IntegerField(max_length=3)
	mobile 	= models.IntegerField(max_length=7)
	class Meta:
		verbose_name = ('Info Phone')
		verbose_name_plural = ('Info Phones')
	def __unicode__(self):
		return "%s %s"%(self.name, self.phone)    





