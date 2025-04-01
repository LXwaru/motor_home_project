from django import forms
from .models import MotorHome, Make, Model

class FilterForm(forms.Form):

    
    make = forms.ModelChoiceField(queryset=Make.objects.all(), required=False)
    model = forms.ModelChoiceField(queryset=Model.objects.all(), required=False)
    year = forms.IntegerField(required=False)
    color = forms.CharField(required=False)
    condition = forms.CharField(required=False)
    price = forms.DecimalField(required=False)
