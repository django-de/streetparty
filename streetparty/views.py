from django.views.generic import ListView
from django.utils import timezone

from .models import StrassenFest


class StrassenFestList(ListView):
    def get_queryset(self):
        qs = StrassenFest.objects.order_by('von')
        form_data = self.request.POST
        if 'von' in form_data and 'bis' in form_data:
            qs = qs.filter(von__gte=form_data['von'], bis__lte=form_data['bis'])
        else:
            today = timezone.now()
            qs = qs.filter(von__year=today.year, von__month=today.month)
        return qs

    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)

class StrassenFestListListing4(ListView):
    def get_queryset(self):
        today = timezone.now()
        return StrassenFest.objects.filter(von__year=today.year, von__month=today.month).order_by('von')
