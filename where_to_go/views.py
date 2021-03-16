from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from places.models import Place, Image
from django.utils import html, safestring

def show_index(request):
    places = {
        "type": "FeatureCollection",
        "features": [
            {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
                },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"places/{place.id}"
                }
            }
            for place in Place.objects.all()
        ]
    }
    context = {
        'places': places
    }
    return render(request, context=context, template_name='index.html')


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = {
        "title": place.title,
        "imgs": place.get_images_urls(),
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        }
    }
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2, })