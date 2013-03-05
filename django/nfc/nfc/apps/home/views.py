from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives # Para enviar HTML
from django.http import HttpResponseRedirect
from nfc.apps.home.forms  import ContactForm
from nfc.apps.customers.models import Customer, ZipCode, Branch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def index_view(request):
	mBranchs = Branch.objects.filter(featured=True).order_by('-id')[:8]
	ctx = {'branchs':mBranchs}
  	return render_to_response('home/home.html',ctx,context_instance=RequestContext(request))

# Funcion para el formulario de contacto
def contact_view(request):
	info_send = False # Define si se envio la info o no se envio
	name   = ""
	email  = ""
	subject = ""
	content  = ""
	if request.method == "POST":
		objForm = ContactForm(request.POST)
		if objForm.is_valid():
			info_send  = True
			name    = objForm.cleaned_data['Name']
			email   = objForm.cleaned_data['Email']
			subject = objForm.cleaned_data['Subject']
			content = objForm.cleaned_data['Content']
			# Configuracion para envio de email por gmail
			to_admin = 'roberto@newemage.com'
			html_content = "Information received from <br>Name: [%s] <br> Email: [%s]  <br><br>***Message<br><br>%s"%(name,email,content)
			msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
			msg.send() #enviamos el correo
	else:
		objForm = ContactForm()

	ctx = {'form':objForm,'name':name,'email':email,'subject':subject,'content':content,'info_send':info_send}
	return render_to_response('forms/contact/contact.html',ctx,context_instance=RequestContext(request))


def my_custom_404_view(request):
	ctx = {'url_to':request.get_full_path}
	return render_to_response('home/404.html',ctx,context_instance=RequestContext(request))
