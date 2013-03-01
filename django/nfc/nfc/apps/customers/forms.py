from django.forms import ModelForm 
from django.db import models
from myproject.apps.customers.models import phone_info


class formInfoPhone(ModelForm):
    class Meta:
        model = phone_info 
