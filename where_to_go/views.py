from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from places.models import Place, Image
from django.utils import html, safestring

def show_index(request):
    value = Place.get_points()
    context = {
        'value': value
    }
    return render(request, context=context, template_name='index.html')


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = place.get_details()
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2, })