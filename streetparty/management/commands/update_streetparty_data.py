from django.core.management.base import NoArgsCommand

from streetparty.helper import StrassenFestHelper


class Command(NoArgsCommand):
    help = 'Holt aktuelle Daten von den Verwaltungsseiten'

    def handle_noargs(self, **options):
        StrassenFestHelper().update()
