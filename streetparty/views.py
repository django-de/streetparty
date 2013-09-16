# Create your views here.
import datetime
from django.views.generic import ListView
from streetparty.models import StrassenFest


class StrassenFestList(ListView):
    #for current month
    today = datetime.date.today()
    queryset = StrassenFest.objects.filter(von__year=today.year, von__month=today.month).order_by("von")

    def post(self, request, *args, **kwargs):
        self.object_list = StrassenFest.objects.filter(von__gte=request.POST['von'], bis__lte=request.POST['bis']).order_by('von')
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
