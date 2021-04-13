from django import forms
from .models import Place
from django.contrib.gis import forms

from leaflet.forms.widgets import LeafletWidget

class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ('title', 'location', 'description', 'address', 'phone', 'city', 'type_of_place', 'tags')
        widgets = {'location': LeafletWidget()}
