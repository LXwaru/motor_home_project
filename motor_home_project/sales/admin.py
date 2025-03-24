from django.contrib import admin
from .models import SalesPerson, Sale   
# Register your models here.
@admin.register(SalesPerson)
class SalesPersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'commission_rate')
    list_filter = ('first_name', 'last_name', 'email', 'phone', 'commission_rate')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'commission_rate')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('motor_home', 'sales_person', 'sale_date', 'sale_price', 'on_hold', 'is_completed', 'warranty_end_date')
    list_filter = ('motor_home', 'sales_person', 'sale_date', 'sale_price', 'on_hold', 'is_completed', 'warranty_end_date')
    search_fields = ('motor_home', 'sales_person', 'sale_date', 'sale_price', 'on_hold', 'is_completed', 'warranty_end_date')

