from django import forms
from .models import ServiceTicket, ServicePerson

class CreateServiceTicketForm(forms.ModelForm):
    motor_home_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = ServiceTicket
        fields = ['service_person', 
                'service_start_date', 
                'service_end_date', 
                'service_description', 
                'service_price', 
                'is_completed', 
                'is_paid', 
                'is_warranty']
    