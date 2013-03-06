# -*- coding: utf-8 -*-
from django.forms import ModelForm 
from django.db import models
from django import forms
from nfc.apps.customers.models import phone_info
from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget
import datetime

class formInfoPhone(ModelForm):
    class Meta:
        model = phone_info 


class frmBirthDate(forms.Form):
	year_choices = [year for year in xrange(int(datetime.datetime.now().year), 1899 , -1)]

	dateofbirth = forms.DateField(
		widget=SelectDateWidget(years=year_choices),
		required=True,
		label='Date of birth'
	)




