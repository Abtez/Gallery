from django import forms
from django.forms import ModelForm
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

CATEGORIES =( 
    ("1", "Anime"), 
    ("2", "Cars"), 
    ("3", "Food"), 
    ("4", "Travel"), 
    ("5", "Abstract"), 
    ("6", "Icons"), 
    ("7", "People"), 
    ("8", "Animals"), 
    ("9", "Nature"), 
    ("10", "Sports"), 
    ("11", "Tech"), 
) 

class ImagesForm(forms.Form):
    image = forms.ImageField(required=True) 
    imagename = forms.CharField(required=True)
    description = forms.CharField(required=True)
    locaton = forms.CharField(required=True)
    category = forms.ChoiceField(choices=CATEGORIES, required=True)