from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.PlaceListView.as_view(), name='list-place'),
    path('places/<int:pk>', views.PlaceDetailView.as_view(), name='detail-place'),
    path('all_cities/', views.all_cities, name='all-cities'),
    path('city/places/<str:inputcity>', views.cityplaces, name='city-places'),
    path('add_place/', views.AddPlace.as_view(), name='add-place'),
    path('add_type_of_place/', views.AddTypeOfPlace.as_view(), name='add-type-of-place'),
]