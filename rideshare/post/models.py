from django.db import models
from django.forms import ModelForm
#from django import forms
#from myapp.models import Article
from django.utils import timezone

class Post(models.Model):
	author = models.CharField(max_length=100)
	seats = models.IntegerField(default=1)
	startLoc = models.CharField(max_length=100)
	endLoc = models.CharField(max_length=100)
	date_ride = models.DateTimeField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	#date_ride = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'))

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.startLoc


		