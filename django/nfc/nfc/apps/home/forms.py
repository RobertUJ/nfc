from django import forms

class ContactForm(forms.Form):
	Name  		= forms.CharField(widget=forms.TextInput())
	Email 		= forms.EmailField(widget=forms.TextInput())
	Subject 	= forms.CharField(widget=forms.TextInput())
	Content 	= forms.CharField(widget=forms.Textarea())