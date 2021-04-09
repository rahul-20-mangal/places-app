from django.shortcuts import render
from django.views import generic
from spot.models import Place

# Create your views here.
def index(request):
    place = Place.objects.distinct('city')
    return render(request, 'index.html', context={"all_places": place})

class PlaceListView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place

def cityplaces(request,inputcity):
    city = Place.objects.filter(city=inputcity)
    return render(request, 'spot/city_places.html', context={'cities':city})




