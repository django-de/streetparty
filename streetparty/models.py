from django.db import models


class StrassenFest(models.Model):
    id = models.IntegerField(primary_key=True)
    bezeichnung = models.TextField()
    #adress-data should normally be normalized
    bezirk = models.CharField(max_length=255, blank=True)
    strasse = models.CharField(max_length=255, blank=True)
    plz = models.CharField(max_length=5, blank=True)
    von = models.DateField()
    bis = models.DateField()
    zeit = models.CharField(max_length=255, blank=True)
    veranstalter = models.TextField(blank=True)
    mail = models.EmailField(blank=True)
    www = models.CharField(max_length=255, blank=True)
    bemerkungen = models.TextField(blank=True)
