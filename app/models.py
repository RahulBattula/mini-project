from django.db import models

from django.utils import timezone
# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(max_length=15)
	
	email=models.EmailField(max_length=25)
	message=models.TextField(max_length=500)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)
	def __str__(self):
		return self.first_name


		
