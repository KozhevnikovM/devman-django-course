import requests
# from app.models import Place
# r = requests.get('https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json')

# title = r.json()['title']
# places = Place.objects.all()

# places.get_or_create(r.json())

from django.core.management.base import BaseCommand, CommandError
from app.models import Place, Image
import json
from urllib.parse import urlparse
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Import place from json'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
    
    def get_place_details(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            place_data = json.loads(file.read())
        place_details = {
            'details_title': place_data['title'],
            'details_description_short': place_data['description_short'],
            'details_description_long': place_data['description_long'],
            'details_lng': place_data['coordinates']['lng'],
            'details_lat': place_data['coordinates']['lat'],
            'imgs': place_data['imgs']
        }
        return place_details

    def handle(self, *args, **options):
        place_details = self.get_place_details(options['filename'])
        urls = place_details.pop('imgs', None)
        place, get_place_result = Place.objects.get_or_create(**place_details)
        if not get_place_result:
            self.stdout.write(self.style.SUCCESS(f'{place} allready exists'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Successfully Added place {place}'))

        
        for url in urls:
            filename = urlparse(url).path.split('/')[-1]
            image, get_image_result = Image.objects.get_or_create(place=place, name=filename)
            if not get_image_result:
                 self.stdout.write(self.style.SUCCESS(f'{image} allready exists'))
                 continue
            response = requests.get(url)
            image.image.save(filename, ContentFile(response.content), save=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully Added {image}'))

        

        
    
