from django.db import models

# Create your models here.
class StrassenFest(models.Model):
    #so, id cannot overwrite the database-id
    api_id = models.CharField(max_length=255, blank=True)
    bezeichnung = models.TextField()
    #adress-data should normally be normalized
    bezirk = models.CharField(max_length=255)
    strasse = models.CharField(max_length=255)
    plz = models.CharField(max_length=5)
    von = models.DateField()
    bis = models.DateField()
    zeit = models.CharField(max_length=255)
    veranstalter = models.TextField()
    mail = models.EmailField()
    www = models.URLField()
    bemerkungen = models.TextField()
