from django.forms import ModelForm
from .models import MotorHome, Make, Model

class MotorHomeForm(ModelForm):
    class Meta:
        model = MotorHome
        fields = '__all__'

class CreateMotorHomeForm(ModelForm):
    class Meta:
        model = MotorHome
        fields = {
            'vin',
            'year',
            'mileage',
            'condition',
            'model_id',
            'color',
            'ticket_price',
            'image',
            'is_new',
            'for_sale',
        }

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