from django.urls import path
from .views import get_inventory, get_motor_home_details, post_inventory, update_motor_home, delete_motor_home

app_name = 'inventory'

urlpatterns = [
    # List view (Read all)
    path('motor_homes/', get_inventory, name='get_inventory'),
    
    # Detail view (Read one)
    path('motor_home/<int:id>/', get_motor_home_details, name='get_motor_home_details'),
    
    # Create view
    path('motor_home/create/', post_inventory, name='post_inventory'),
    
    # Update view
    path('motor_home/<int:id>/update/', update_motor_home, name='update_motor_home'),
    
    # Delete view
    path('motor_home/<int:id>/delete/', delete_motor_home, name='delete_motor_home')
]
