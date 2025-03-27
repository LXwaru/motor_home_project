from django import forms
from .models import ServiceTicket, ServicePerson, ServiceItem

class CreateServiceTicketForm(forms.ModelForm):
    service_start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    motor_home_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        motor_home_id = kwargs.pop('motor_home_id', None)
        super().__init__(*args, **kwargs)
        if motor_home_id:
            self.fields['motor_home_id'].initial = motor_home_id
            
    class Meta:
        model = ServiceTicket
        fields = [
            'motor_home_id', 
            'service_person', 
            'service_start_date', 
        ]
    
class EditServiceTicketForm(forms.ModelForm):
    class Meta:
        model = ServiceTicket
        fields = [
            'service_person', 
            'service_price'
        ]

class AddServiceItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        service_ticket_id = kwargs.pop('service_ticket_id', None)
        super().__init__(*args, **kwargs)
        if service_ticket_id:
            self.fields['service_ticket'].initial = service_ticket_id
            self.fields['service_ticket'].widget = forms.HiddenInput()

    class Meta:
        model = ServiceItem
        fields = ['service_ticket', 'item_description', 'item_price']