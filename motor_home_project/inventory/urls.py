from django.urls import path
from .views import get_inventory, get_motor_home_details, post_inventory, update_motor_home, delete_motor_home, add_make, add_model

app_name = 'inventory'

urlpatterns = [
    # List view (Read all)
    path('', get_inventory, name='get_inventory'),
    
    # Detail view (Read one)
    path('detail/<int:id>/', get_motor_home_details, name='get_motor_home_details'),
    
    # Create view
    path('create/', post_inventory, name='post_inventory'),
    
    # Update form view
    path('update/form/<int:id>/', update_motor_home, name='motor_home_update_form'),
    
    # Update action
    path('update/<int:id>/', update_motor_home, name='update_motor_home'),

    # Delete view
    path('delete/<int:id>/', delete_motor_home, name='delete_motor_home'),

    # Add make
    path('add_make/', add_make, name='add_make'),

    # Add model
    path('add_model/', add_model, name='add_model'),
]
