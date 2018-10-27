from django import forms
import datetime
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('startLoc','endLoc','seats','date_ride',)
