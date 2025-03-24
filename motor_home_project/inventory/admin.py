from django.contrib import admin
from .models import Make, ModelVehicle, MotorHome
# Register your models here.
@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(ModelVehicle)
class ModelVehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'make')
    list_filter = ('name', 'make')
    search_fields = ('name', 'make__name')


@admin.register(MotorHome)
class MotorHomeAdmin(admin.ModelAdmin):
    list_display = ('vin', 'year', 'model', 'color', 'ticket_price', 'is_new', 'for_sale', 'is_sold', 'sold_date')
    list_filter = ('year', 'model', 'color', 'is_new', 'for_sale', 'is_sold')
    search_fields = ('vin', 'model__name', 'color')



