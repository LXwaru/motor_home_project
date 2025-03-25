from django.forms import ModelForm
from .models import MotorHome

class MotorHomeForm(ModelForm):
    class Meta:
        model = MotorHome
        fields = '__all__'