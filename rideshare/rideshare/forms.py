from django import forms
import datetime
from .models import Post

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('startLoc','endLoc','seats','date_ride')
    date_ride = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', ))