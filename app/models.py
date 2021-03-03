from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    description_short = models.CharField(max_length=400)
    description_long = models.TextField()
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()