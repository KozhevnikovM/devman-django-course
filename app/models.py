from django.db import models
from django.utils import html
from django.shortcuts import get_list_or_404
from django.core import serializers

# Create your models here.
class Place(models.Model):
    id = models.AutoField(primary_key=True)

    point_lng = models.FloatField()
    point_lat = models.FloatField()

    properties_title = models.CharField(max_length=200, help_text='Название точки на карте')
    properties_place_id = models.CharField(max_length=200, unique=True, help_text='ID точки')

    details_title = models.CharField(max_length=200, help_text='Заголовок')
    details_description_short = models.CharField(max_length=400, help_text='Краткое описание')
    details_description_long = models.TextField()
    details_lng = models.FloatField()
    details_lat = models.FloatField()

    def get_details(self):
        return {
            "title": self.details_title,
            "imgs": self.get_images_urls(),
            "description_short": self.details_description_short,
            "description_long": self.details_description_long,
            "coordinates": {
                "lat": self.details_lat,
                "lng": self.details_lng,
            }
        }
        

    def get_images_urls(self):
        return [item.image.url for item in get_list_or_404(Image, place=self)]
    
    @classmethod
    def get_points(cls):
        return {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.point_lng, place.point_lat]
                },
                "properties": {
                    "title": place.properties_title,
                    "placeId": place.properties_place_id,
                    "detailsUrl": f"places/{place.id}"

                }
                }
                for place in cls.objects.all()]
            }

    def __str__(self):
        return self.properties_title


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    name = models.CharField(max_length=200)
    order = models.SmallIntegerField(unique=False, default=1)
    place = models.ForeignKey(to='Place', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.order} {self.name}'
    
    class Meta:
        ordering = ['order']
        