from django.http import HttpResponse
from django.shortcuts import render
from app.models import Place, Image

def show_index(request):
    places = Place.objects.all()
    images = Image.objects.all().filter(place=places[0])

    value = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.coordinates_lng, place.coordinates_lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.title,
            "detailsUrl": "static/places/moscow_legends.json"

          }
        } for place in places
      ]
    }
    context = {
        'value': value
    }
    return render(request, context=context, template_name='index.html')