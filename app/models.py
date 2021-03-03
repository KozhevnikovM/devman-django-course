from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    description_short = models.CharField(max_length=400)
    description_long = models.TextField()
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200, primary_key=True)
    order = models.SmallIntegerField(unique=True, default=0)
    place = models.ForeignKey(to='Place', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.order} {self.name}'
    
    class Meta:
        ordering = ['order']
        