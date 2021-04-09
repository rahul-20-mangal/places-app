from django.db import models
from django.contrib.gis.db.models import PointField
# Create your models here.

class Place(models.Model):
    location = PointField(null=True)