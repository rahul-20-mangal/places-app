from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.PlaceListView.as_view(), name='list-place'),
    path('places/<int:pk>', views.PlaceDetailView.as_view(), name='detail-place'),
    
]