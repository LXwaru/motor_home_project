from django import forms
from .models import Employee

class CreateEmployeeForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zip_code = forms.CharField(required=True)
    is_service_provider = forms.BooleanField(required=False)
    is_sales_person = forms.BooleanField(required=False)
    username = forms.CharField(required=False, widget=forms.HiddenInput())
    is_active = forms.BooleanField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = Employee
        fields = ['full_name', 
                'email',
                'password',
                'phone_number',
                'address',
                'city',
                'state',
                'zip_code', 
                'is_service_provider', 
                'is_service_admin',
                'is_sales_person',
                'is_sales_admin',
                'is_active'
        ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email:
            cleaned_data['username'] = email
        cleaned_data['is_active'] = True
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())   

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        return cleaned_data 
    
class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'phone_number', 'address', 'city', 'state', 'zip_code', 
        'is_service_provider', 'is_sales_person', 'is_service_admin', 'is_sales_admin'] 