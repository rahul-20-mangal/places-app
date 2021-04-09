from django.db import models
from django.contrib.gis.db.models import PointField
# Create your models here.

class Place(models.Model):
    title = models.CharFiled(max_length=200)
    location = PointField(null=True)
    description = models.TextField(max_length=2000)
    address = models.CharFiled(max_length=200)
    phone = models.IntegerField()
    city = models.CharFiled(max_length=200)
    type_of_place = models.CharFiled(max_length=200)
    tags = models.CharFiled(max_length=200)
