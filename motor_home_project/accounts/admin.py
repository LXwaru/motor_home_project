from django.contrib import admin
from .models import Employee, Customer
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'phone_number', 'is_service_provider', 'is_sales_person', 'is_service_admin', 'is_sales_admin', 'is_active')
    list_filter = ('is_service_provider', 'is_sales_person', 'is_service_admin', 'is_sales_admin', 'is_active')
    search_fields = ('username', 'full_name', 'email', 'phone_number')
    list_per_page = 10
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email', 'phone_number')
    list_per_page = 10
    
