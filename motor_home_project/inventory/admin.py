from django.contrib import admin
from .models import Make, Model, MotorHome
# Register your models here.
@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make_id')
    list_filter = ('name', 'make_id')
    search_fields = ('name', 'make_id__name')


@admin.register(MotorHome)
class MotorHomeAdmin(admin.ModelAdmin):
    list_display = ('vin', 'year', 'model_id', 'color', 'ticket_price', 'is_new', 'for_sale', 'is_sold', 'sold_date')
    list_filter = ('year', 'model_id', 'color', 'is_new', 'for_sale', 'is_sold')
    search_fields = ('vin', 'model_id__name', 'color')



