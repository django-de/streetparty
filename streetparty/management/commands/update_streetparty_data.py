import sys
import json
import urllib2
from datetime import datetime

from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import ValidationError

from streetparty.models import StrassenFest


class Command(NoArgsCommand):
    help = 'Holt aktuelle Daten von den Verwaltungsseiten'

    def handle_noargs(self, **options):
        req = urllib2.Request(settings.STREETPARTY_DATA_URL)
        opener = urllib2.build_opener()
        source = opener.open(req)

        for data in json.load(source)['index']:
            # This API is so broken.
            data['von'] = datetime.strptime(data['von'], '%Y-%m-%d')
            data['bis'] = datetime.strptime(data['bis'], '%d.%m.%Y')
            # save figures out whether to update or to insert by using
            # the remote id as primary key.
            fest = StrassenFest(**data)
            try:
                fest.full_clean(exclude=['id'])
            except ValidationError as e:
                print >>sys.stderr, 'Failed to validate remote entry with id %s' % data['id']
                print >>sys.stderr, str(e)
            else:
                fest.save()
