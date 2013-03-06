# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives # Para enviar HTML
from django.http import HttpResponseRedirect
from django.http import Http404
from django.http import HttpResponse
from nfc.apps.customers.forms import frmBirthDate
from nfc.apps.customers.models import ZipCode,Customer,Branch,PhotoGallery 
from nfc.apps.customers.forms import formInfoPhone
import datetime


def get_customer(request,customer,zipcode,branch):
	_slug_customer = str(customer)
	_zipcode  = int(zipcode)
	_slug_branch   = str(branch)
	
	mCustomer 	= 	get_object_or_404(Customer,slug=_slug_customer)
	mZipCode 	= 	get_object_or_404(ZipCode,zipcode=_zipcode)
	mBranch 	= 	get_object_or_404(Branch,Customer=mCustomer,ZipCode=mZipCode,slug=_slug_branch)

	try:
		mGalery = PhotoGallery.objects.filter(Branch=mBranch)
	except PhotoGallery.DoesNotExist:
		mGalery = None
	
	""" Formulario para la peticion de numero de telefono """
	if request.method == "POST":
		mformPhone = formInfoPhone(request.POST)
		if mformPhone.is_valid():
			mfrmPhoneUncommited = mformPhone.save(commit=False)
			mfrmPhoneUncommited.branch = mBranch
			mfrmPhoneUncommited.save()

			ctx = {'branch':mBranch,'last_url':request.get_full_path}
			return render_to_response('customers/image_view.html',ctx,context_instance=RequestContext(request))
		else:
			mformPhone = formInfoPhone()

	else:
		mformPhone = formInfoPhone()

	""" Check adult_required field """
	flag = bool(request.session.get(mBranch.slug,False))
	if mBranch.adult_required and not flag:
		if request.method == 'POST':
			frm = frmBirthDate(request.POST)
			if frm.is_valid():
				dateBirth = frm.cleaned_data.get('dateofbirth')
				now = datetime.date.today()
				diff = now - dateBirth
				years = int(diff.days / 365)
				if not years >= int(mBranch.age_required):
					ctx = {'infobranch':mBranch,'form':frm, 'msg':"Sorry, you must be at least %s old years to enter this website."%int(mBranch.age_required)}
					return render_to_response('customers/form_age.html',ctx,context_instance=RequestContext(request))
				else:
					request.session[mBranch.slug] = True
			else:
				ctx = {'infobranch':mBranch,'form':frm}
				return render_to_response('customers/form_age.html',ctx,context_instance=RequestContext(request))
		else:
			print mBranch
			ctx = {'infobranch':mBranch,'form':frmBirthDate()}
			return render_to_response('customers/form_age.html',ctx,context_instance=RequestContext(request))


	ctx = {'infobranch':mBranch,'galery':mGalery,'frmPhone':mformPhone}
	return render_to_response('customers/customer.html',ctx,context_instance=RequestContext(request))


def get_all_branchs(request,customer,zipcode):
	_slug_customer = str(customer)
	_zipcode  = int(zipcode)
	mZipCode 	= 	get_object_or_404(ZipCode,zipcode=_zipcode)
	mcustomer 	= 	get_object_or_404(Customer,slug=_slug_customer)
	mBranch 	= 	Branch.objects.filter(ZipCode=mZipCode,Customer=mcustomer).order_by('-id')

	ctx = {'branchs':mBranch}
	return render_to_response('customers/allbranchs.html',ctx,context_instance=RequestContext(request))
	

	




