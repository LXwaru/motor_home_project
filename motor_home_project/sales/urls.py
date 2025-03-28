from django.urls import path
from . import views

urlpatterns = [
    path('for-sale/', views.for_sale_view, name='for_sale'),
]
