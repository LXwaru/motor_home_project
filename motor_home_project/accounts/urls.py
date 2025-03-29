from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.create_employee, name='create_employee'),
    path('', views.list_employees, name='list_employees'),
    path('profile/<int:id>/', views.profile_employee, name='profile_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('deactivate/<int:id>/', views.deactivate_employee, name='deactivate_employee'),
    path('activate/<int:id>/', views.activate_employee, name='activate_employee'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]   