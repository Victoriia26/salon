from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from salon.models import Record, Master
from .forms import SalonForm, DateForm


# class SalonListView(generic.ListView):
#     model = Record
#     template_name = 'index.html'
#     context_object_name = 'salon'

def index(request):
    salons = Master.objects.all()
    return render(request, 'index.html', locals())

class SalonCreateView(generic.CreateView):
    # model = Car
    form_class = SalonForm
    template_name = 'salon_crud/create.html'
    success_url = reverse_lazy('index')
