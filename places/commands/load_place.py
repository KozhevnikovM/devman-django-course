import requests
# from places.models import Place
# r = requests.get('https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json')

# title = r.json()['title']
# places = Place.objects.all()

# places.get_or_create(r.json())

from django.core.management.base import BaseCommand, CommandError
from places.models import Place

class Command(BaseCommand):
    help = 'Import place from json'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        pass

    self.stdout.write(self.style.SUCCESS('Successfully closed poll'))