from django.core.management.base import BaseCommand

from streetparty.helper import StrassenFestHelper


class Command(BaseCommand):
    help = 'Holt aktuelle Daten von den Verwaltungsseiten'

    def handle(self, *args, **options):
        StrassenFestHelper().update()
