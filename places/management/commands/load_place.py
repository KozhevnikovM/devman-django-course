import requests
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
import json
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Import place from json'

    def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--url', type=str, help='Url to global json file')
        group.add_argument('--path', type=str, help='Path to local json file')

    def load_json_from_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.loads(file.read())

    def load_json_from_url(self, url):
        response = requests.get(url)
        if response.ok:
            return response.json()

    def get_place_details(self, json_data):
        place_details = {
            'title': json_data['title'],
            'short_description': json_data['description_short'],
            'long_description': json_data['description_long'],
            'lng': json_data['coordinates']['lng'],
            'lat': json_data['coordinates']['lat'],
            'imgs': json_data['imgs']
        }
        return place_details

    def handle(self, *args, **options):
        json_data = self.load_json_from_url(options['url']) if options['url'] else self.load_json_from_file(options['path'])
        place_details = self.get_place_details(json_data)
        urls = place_details.pop('imgs', None)
        place, get_place_result = Place.objects.get_or_create(title=place_details['title'], defaults=place_details)
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
