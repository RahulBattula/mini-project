from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		exclude = ['date', 'time']
		widgets={
		'first_name':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.TextInput(attrs={'class':'form-control'}),
		'message':forms.TextInput(attrs={'class':'form-control'}),
		}
