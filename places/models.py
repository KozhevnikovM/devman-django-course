from django.db import models
from django.utils import html
from django.shortcuts import get_list_or_404
from django.core import serializers
from tinymce.models import HTMLField
from django.http import Http404

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Подробное описание', blank=True)
    lng = models.FloatField(verbose_name='Координата по долготе')
    lat = models.FloatField(verbose_name='Координата по широте')
    
    def get_images_urls(self):
        return [image.image.url for image in self.images.all()]

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Файл изображения')
    name = models.CharField(max_length=200, blank=True, default=image.name, editable=False)
    order = models.SmallIntegerField(unique=False, blank=True, null=True, verbose_name='Номер фотографии в списке')
    place = models.ForeignKey(to='Place', on_delete=models.SET_NULL, null=True, verbose_name='Место', related_name='images')

    def __str__(self):
        if not self.image:
            return
        return f'{self.order} {self.image}'
    
    class Meta:
        ordering = ['order']
        