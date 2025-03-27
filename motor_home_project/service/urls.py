from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
        path('', views.service_waiting_list, name='service_waiting_list'),
        path('create/<int:motor_home_id>/', views.create_service_ticket, name='create_service_ticket'),
        path('open_tickets/', views.open_service_ticket_list, name='open_service_ticket_list'),
        path('close_ticket/<int:ticket_id>/', views.close_service_ticket, name='close_service_ticket'),
        path('edit_ticket/<int:ticket_id>/', views.edit_service_ticket, name='edit_service_ticket'),
        path('service_history/', views.list_service_history, name='list_service_history'),
        path('add_item/<int:ticket_id>/', views.add_service_item, name='add_service_item'),
        path('remove_item/<int:item_id>/', views.remove_service_item, name='remove_service_item'),
    ]
    