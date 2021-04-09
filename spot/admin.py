from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Place

# Register your models here.

admin.site.register(Place)




