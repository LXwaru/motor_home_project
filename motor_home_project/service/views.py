from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import MotorHome
from service.models import ServiceTicket, ServiceItem
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from service.forms import CreateServiceTicketForm, EditServiceTicketForm, AddServiceItemForm
from datetime import datetime
# Create your views here.


@require_http_methods(['GET'])
def service_waiting_list(request):
    if request.method == 'GET':
        # Get motorhomes that are marked for service but don't have any service tickets
        vehicle_waiting_list = MotorHome.objects.filter(
            for_service=True
        ).exclude(
            id__in=ServiceTicket.objects.values_list('motor_home_id', flat=True)
        )
        
        context = {
            'vehicle_waiting_list': vehicle_waiting_list,
        }
        return render(request, 'service/vehicle_list.html', context)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@require_http_methods(['GET', 'POST'])
def create_service_ticket(request, motor_home_id):  
    motor_home = get_object_or_404(MotorHome, id=motor_home_id)
    if request.method == 'GET':
        form = CreateServiceTicketForm(motor_home_id=motor_home_id)
        print(motor_home_id, "motor_home_id")
        return render(request, 'service/create_service_ticket.html', {'form': form, 'motor_home': motor_home})
    elif request.method == 'POST':
        form = CreateServiceTicketForm(request.POST, motor_home_id=motor_home_id)
        if form.is_valid():
            service_ticket = form.save(commit=False)
            service_ticket.motor_home = motor_home
            service_ticket.save()
            return redirect('service:open_service_ticket_list')
        else:
            return render(request, 'service/create_service_ticket.html', {'form': form, 'motor_home': motor_home})


@require_http_methods(['GET'])
def open_service_ticket_list(request):
    service_tickets = ServiceTicket.objects.filter(is_completed=False)
    context = {
        'service_tickets': service_tickets,
    }
    return render(request, 'service/open_ticket_list.html', context)


def close_service_ticket(request, ticket_id):
    ticket = get_object_or_404(ServiceTicket, id=ticket_id)
    ticket.is_completed = True
    ticket.service_end_date = datetime.now()
    ticket.is_paid = True
    ticket.save()
    return redirect('service:open_service_ticket_list')

@require_http_methods(['GET', 'POST'])
def edit_service_ticket(request, ticket_id):
    ticket = get_object_or_404(ServiceTicket, id=ticket_id)
    if request.method == 'GET':
        form = EditServiceTicketForm(instance=ticket)
        return render(request, 'service/update_ticket.html', {'form': form, 'ticket': ticket})
    elif request.method == 'POST':
        form = EditServiceTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('service:open_service_ticket_list')
        else:
            return render(request, 'service/edit_service_ticket.html', {'form': form, 'ticket': ticket})

@require_http_methods(['GET'])
def list_service_history(request):
    service_history = ServiceTicket.objects.filter(is_completed=True)
    service_items = ServiceItem.objects.filter(service_ticket__in=service_history)
    context = {
        'service_history': service_history,
        'service_items': service_items,
    }
    return render(request, 'service/service_history.html', context)


@require_http_methods(['GET','POST'])
def add_service_item(request, ticket_id):
    if request.method == 'GET':
        form = AddServiceItemForm(service_ticket_id=ticket_id)
        return render(request, 'service/create_service_item.html', {'form': form})
    elif request.method == 'POST':
        form = AddServiceItemForm(request.POST, service_ticket_id=ticket_id)
        if form.is_valid():
            form.save()
            ticket = get_object_or_404(ServiceTicket, id=ticket_id)
            ticket.service_price = sum(item.item_price for item in ticket.items.all())
            ticket.save()
            return redirect('service:open_service_ticket_list')
        else:
            return render(request, 'service/create_service_item.html', {'form': form})


@require_http_methods(['POST'])
def remove_service_item(request, item_id):
    item = get_object_or_404(ServiceItem, id=item_id)
    ticket = item.service_ticket
    item.delete()
    # Update the ticket subtotal after removing the item
    ticket.service_price = sum(item.item_price for item in ticket.items.all())
    ticket.save()
    return redirect('service:open_service_ticket_list')