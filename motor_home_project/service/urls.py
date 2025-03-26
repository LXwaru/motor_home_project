from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
        path('', views.service_list, name='service_list'),
        path('create/<int:motor_home_id>/', views.create_service_ticket, name='create_service_ticket'),
    ]
