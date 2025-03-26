from django import forms
from django.forms import ModelForm
from .models import MotorHome, Make, Model

class MotorHomeForm(ModelForm):
    class Meta:
        model = MotorHome
        fields = '__all__'

class CreateMotorHomeForm(ModelForm):
    model_id = forms.ModelChoiceField(
        queryset=Model.objects.all(),
        label="Make - Model"
    )
    class Meta:
        model = MotorHome
        fields = [
            'vin',
            'model_id',
            'year',
            'color',
            'mileage',
            'condition',
            'ticket_price',
            'image',
            'is_new',
            'for_sale',
            'for_service',
            'for_rental',
        ]

class AddMakeForm(ModelForm):
    class Meta:
        model = Make
        fields = {
            'name',
        }

class AddModelForm(ModelForm):
    class Meta:
        model = Model
        fields = {
            'name',
            'make_id',
        }