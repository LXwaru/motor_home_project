from django.urls import path
from .views import get_inventory, get_motor_home_details, post_inventory, update_motor_home, delete_motor_home, add_make, add_model

app_name = 'inventory'

urlpatterns = [
    path('', get_inventory, name='get_inventory'),
    path('detail/<int:id>/', get_motor_home_details, name='get_motor_home_details'),
    path('create/', post_inventory, name='post_inventory'),
    path('update/form/<int:id>/', update_motor_home, name='motor_home_update_form'),
    path('update/<int:id>/', update_motor_home, name='update_motor_home'),
    path('delete/<int:id>/', delete_motor_home, name='delete_motor_home'),
    path('add_make/', add_make, name='add_make'),
    path('add_model/', add_model, name='add_model'),
]
