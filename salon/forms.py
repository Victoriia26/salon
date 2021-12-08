from django.core.validators import RegexValidator
from salon.models import Record, Customer
from django import forms


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M'])


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_number(self):
        num = self.cleaned_data['number']
        validator = RegexValidator("[+]996\d{9}")
        validator(num)
        return num


class SalonForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = "__all__"
        widgets = {'customer': forms.HiddenInput()}
        # exclude = ('customer',)
