from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'startLoc','endLoc','seats','date_ride','published_date')