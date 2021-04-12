from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    
    class Meta:
        model = Place
        fields = ('title', 'description', 'address', 'phone', 'city', 'type_of_place', 'tags')
