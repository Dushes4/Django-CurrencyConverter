from django import forms

from .models import Rate


class ConverterForm(forms.Form):
    from_currency = forms.ModelChoiceField(label="From", queryset=Rate.objects.all(), required=True)
    to_currency = forms.ModelChoiceField(label="To", queryset=Rate.objects.all(), required=True)
    value = forms.FloatField(required=False, min_value=0)

    value.widget = forms.NumberInput(attrs={'class': 'field'})
