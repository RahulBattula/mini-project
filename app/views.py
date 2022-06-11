from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from django import forms
from django.forms import Form
from django.shortcuts import render, get_object_or_404
#import pytz
# Create your views here.


	
def home(request):
	return render(request,'home.html')
	
def security(request):
	return render(request,'security.html')
	
#def contact(request):
	#return render(request,'contact.html')
	
def about_us(request):
	return render(request,'about.html')
	
def intermediate(request):
	return render(request,'intermediate.html')
	
def paramedical_courses(request):
	return render(request,'para.html')
	
def diploma(request):
	return render(request,'diploma.html')
	
def iti(request):
	return render(request,'iti.html')
	
def paramedical(request):
	return render(request,'para.html')
	
def vocational(request):
	return render(request,'vocational.html')
	
def menstruation(request):
	return render(request,'mens.html')
	
def fertility(request):
	return render(request,'mens.html')

	
def depression(request):
	return render(request,'dep.html')
	
def thy(request):
	return render(request,'thy.html')
	
def fertility(request):
	return render(request,'fertility.html')
	
def cancer(request):
	return render(request,'cancer.html')

def feedback(request):
	return render(request,'feedback.html')

def login(request):
    return render(request,'login.html')

	
def index(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form)
			form.save()
	context = {'form': form}
	return render(request,'index.html',context) 
   
def get_details(request):
	data=Contact.objects.all()
	context = {'data': data}
	return render(request,'details.html',context)

def register(request):
    form = UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered.')
				



