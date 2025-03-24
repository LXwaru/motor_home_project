from django.contrib import admin
from .models import ServicePerson, ServiceTicket    

# Register your models here.
@admin.register(ServicePerson)
class ServicePersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('first_name', 'last_name', 'email', 'phone')
    
    

@admin.register(ServiceTicket)
class ServiceTicketAdmin(admin.ModelAdmin):
    list_display = ('motor_home', 'service_person', 'service_date', 'service_description', 'service_price', 'is_completed', 'is_paid', 'is_warranty')
    search_fields = ('motor_home', 'service_person', 'service_date', 'service_description', 'service_price', 'is_completed', 'is_paid', 'is_warranty')
    list_filter = ('motor_home', 'service_person', 'service_date', 'service_description', 'service_price', 'is_completed', 'is_paid', 'is_warranty')