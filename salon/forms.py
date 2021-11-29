from django.forms import ModelForm
from salon.models import Record, Customer, Master
from django import forms


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class SalonForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ("__all__")


