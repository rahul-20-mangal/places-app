from django.shortcuts import render, redirect
from django.views import generic
from spot.models import Place, TypeOfPlace
from spot.forms import PlaceForm, TypeOfPlaceForm
from django.contrib.gis.db.models import PointField
from django.urls import reverse
# Create your views here.
def index(request):
    
    return render(request, 'index.html')

class PlaceListView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place

def all_cities(request):
    place = Place.objects.distinct('city')
    return render(request, 'spot/all_cities.html', context={"all_places": place})

def cityplaces(request, inputcity):
    city = Place.objects.filter(city=inputcity)
    return render(request, 'spot/city_places.html', context={'cities':city})

class AddPlace(generic.CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'spot/add_place.html'

class AddTypeOfPlace(generic.CreateView):
    model = TypeOfPlace
    form_class = TypeOfPlaceForm
    template_name = 'spot/add_type_of_place.html'
    def get_success_url(self):
        return reverse('add-place')




