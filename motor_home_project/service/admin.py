from django.contrib import admin
from .models import ServiceTicket, ServicePerson, ServiceItem

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1

class ServiceTicketAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'motor_home', 
        'service_provider', 
        'service_start_date',
        'service_price',
        'is_completed',
        'is_paid',
        'is_warranty'
    ]
    list_filter = [
        'service_provider',
        'service_start_date',
        'is_completed',
        'is_paid',
        'is_warranty'
    ]
    inlines = [ServiceItemInline]

admin.site.register(ServiceTicket, ServiceTicketAdmin)
admin.site.register(ServiceItem)