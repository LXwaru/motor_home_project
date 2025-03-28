from django.shortcuts import render, get_object_or_404
from .models import MotorHome

def for_sale_view(request):
    motor_homes = MotorHome.objects.filter(for_sale=True)
    
    sort = request.GET.get('sort', '')
    
    if sort == 'price_asc':
        motor_homes = motor_homes.order_by('ticket_price')
    elif sort == 'price_desc':
        motor_homes = motor_homes.order_by('-ticket_price')
    elif sort == 'year_asc':
        motor_homes = motor_homes.order_by('year')
    elif sort == 'year_desc':
        motor_homes = motor_homes.order_by('-year')

    return render(request, 'sales/for_sale.html', {
        'motor_homes': motor_homes
    })
