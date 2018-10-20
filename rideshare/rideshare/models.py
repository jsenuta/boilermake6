from django.db import models
from django.forms import ModelForm
#from myapp.models import Article
from django.utils import timezone

class Post(models.Model):
	author = models.CharField(max_length=100)
	seats = models.IntegerField(default=1)
	startLoc = models.CharField(max_length=100)
	endLoc = models.CharField(max_length=100)
	date_ride = models.DateTimeField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.startLoc

class Choice(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

"""class PostForm(ModelForm):
	class Meta:
		model = Article
		fields = ['pub_date', 'ride_date', 'content', 'start', 'end']

	def publish(self):
		self.pub_date = timezone.now()
		self.save()
#form = PostForm()
#article = Article.objects.get(pk=1)
#form = PostForm(instance=article)"""

