from django.core.management.base import BaseCommand, CommandError
from ...models import Author


class Command(BaseCommand):
    help = "list all the authors"

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        return Author.objects.filter(name__endswith = 'h')
