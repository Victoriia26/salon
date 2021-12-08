from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from salon.models import Record, Master, Services
from .forms import SalonForm, CustomerForm

class SalonListView(generic.ListView):
    model = Master
    template_name = 'index.html'
    context_object_name = 'masters'

class RecordListView(generic.ListView):
    model = Record
    template_name = 'salon_crud/record.html'
    context_object_name = 'records'


class RecordDetailView(generic.DetailView):
    model = Record
    template_name = 'salon_crud/detail.html'
    context_object_name = 'record'


class ServisListView(generic.ListView):
    model = Services
    template_name = 'services.html'
    context_object_name = 'servis'

class RecordUpdateView(generic.UpdateView):
    model = Record
    fields = ('branch', 'service', 'master', 'record_time',)

    success_url = '../../record/'


def delete_post(request, pk):
    record = get_object_or_404(Record, id=pk)
    record.delete()
    return redirect('records')

def create_salon(request):
    form = SalonForm
    form1 = CustomerForm
    if request.method == 'POST':
        form = SalonForm(request.POST)
        form1 = CustomerForm(request.POST)
        if form.is_valid() and form1.is_valid():
            print(form.cleaned_data, 'cleaned data')
            x = form1.save()
            salon = form.save(commit=False)
            salon.customer = x
            salon.save()
            form.save_m2m()
            return redirect('records')

    return render(request, 'salon_crud/create.html', locals())
