import requests
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
import json
from urllib.parse import urlparse
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Import place from json'

    def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--url', type=str, help='Url to global json file')
        group.add_argument('--path', type=str, help='Path to local json file')

    def get_place_details(self, raw_place):
        place_details = {
            'title': raw_place['title'],
            'short_description': raw_place['description_short'],
            'long_description': raw_place['description_long'],
            'lng': raw_place['coordinates']['lng'],
            'lat': raw_place['coordinates']['lat'],
            'imgs': raw_place['imgs']
        }
        return place_details

    def handle(self, *args, **options):
        if options['url']:
            response = requests.get(options['url'])
            response.raise_for_status()
            raw_place = response.json()
            if 'error' in raw_place:
                raise requests.exceptions.HTTPError(raw_place['error'])
        
        if options['path']:
            with open(options['path'], 'r', encoding='utf-8') as file:
                raw_place = json.loads(file.read())
        
        place_details = self.get_place_details(raw_place)
        urls = place_details.pop('imgs', None)
        place, created = Place.objects.get_or_create(title=place_details['title'], defaults=place_details)
        if not created:
            self.stdout.write(self.style.SUCCESS(f'{place} allready exists'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Successfully Added place {place}'))

        
        for url in urls:
            filename = urlparse(url).path.split('/')[-1]
            image, created = Image.objects.get_or_create(place=place, name=filename)
            if not created:
                 self.stdout.write(self.style.SUCCESS(f'{image} allready exists'))
                 continue
            response = requests.get(url)
            response.raise_for_status()
            image.image.save(filename, ContentFile(response.content), save=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully Added {image}'))
