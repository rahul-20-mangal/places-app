from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Place, TypeOfPlace

# Register your models here.

@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    default_lon = 8754379
    default_lat = 2557588
    default_zoom = 4

admin.site.register(TypeOfPlace)