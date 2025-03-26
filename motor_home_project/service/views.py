from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import MotorHome
from service.models import ServiceTicket
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from service.forms import CreateServiceTicketForm
# Create your views here.


@require_http_methods(['GET'])
def service_list(request):
    if request.method == 'GET':
        motor_homes_for_service = MotorHome.objects.filter(for_service=True)
        context = {
            'motor_homes': motor_homes_for_service,
        }
        return render(request, 'service/list.html', context)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@require_http_methods(['GET', 'POST'])
def create_service_ticket(request, motor_home_id):  
    if request.method == 'GET':
        form = CreateServiceTicketForm()
        return render(request, 'service/create_service_ticket.html', {'form': form})
    elif request.method == 'POST':
        form = CreateServiceTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service:service_list')
    return render(request, 'service/create_service_ticket.html', {'form': form})


