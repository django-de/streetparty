import json
import urllib2
from datetime import datetime
from lmartikel.settings import DATA_URL
from streetparty.models import StrassenFest


class StrassenFestHelper():
    def update_alternative(self):
        """
        this alternative does not update,
        but deletes all before wrtiting to database
        you could use it if you dont know if the remote-id is unique
        and extend it with an update-function...
        """
        #open data-url
        req = urllib2.Request(DATA_URL)
        opener = urllib2.build_opener()
        source = opener.open(req)

        #avoid writing an update-routine
        StrassenFest.objects.all().delete()

        for data in json.load(source)['index']:
            data['bis'] = datetime.strptime(data["bis"], "%d.%m.%Y")
            #run through all keys and check for problems
            for key in data.iterkeys():

                #overwrite id with api_id, to not use database-id
                key = (lambda key: key if key != "id" else 'api_id')(key)

            StrassenFest(**data).save()
