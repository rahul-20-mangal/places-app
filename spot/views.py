from django.shortcuts import render
from django.views import generic
from spot.models import Place

# Create your views here.
def index(request):
    place = Place.objects.all()
    return render(request, 'index.html', context={"all_places": place})

class PlaceListView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place




