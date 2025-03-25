from django.shortcuts import render, get_object_or_404, redirect
from .models import MotorHome, Model
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
from .forms import MotorHomeForm


@require_http_methods(['GET'])
def get_inventory(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        motor_homes = MotorHome.objects.select_related('model_id', 'model_id__make_id').all()
        context = {
            'motor_homes': motor_homes
        }
        
        return render(request, 'inventory/list.html', context)

@ensure_csrf_cookie
@require_http_methods(['POST'])
def post_inventory(request):
    if request.method == 'POST':
        try:
            content = json.loads(request.body)
            model = get_object_or_404(Model, id=content['model_id'])
            motor_home = MotorHome.objects.create(
                vin=content['vin'],
                year=content['year'],
                mileage=content['mileage'],
                condition=content['condition'],
                model_id=model,
                color=content['color'],
            )
            return JsonResponse({'message': 'Created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

@require_http_methods(['GET'])
def get_motor_home_details(request, id):
    if request.method == 'GET':
        motor_home = get_object_or_404(MotorHome, id=id)
        context = {
            'motor_home': motor_home
        }
        return render(request, 'inventory/detail.html', context)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@ensure_csrf_cookie
@require_http_methods(['GET', 'POST'])
def update_motor_home(request, id):
    if request.method == 'GET':
        motor_home = get_object_or_404(MotorHome, id=id)
        form = MotorHomeForm(instance=motor_home)
        context = {
            'motor_home': motor_home,
            'form': form
        }
        return render(request, 'inventory/update.html', context)
    elif request.method == 'POST':
        motor_home = get_object_or_404(MotorHome, id=id)
        form = MotorHomeForm(request.POST, request.FILES, instance=motor_home)
        if form.is_valid():
            form.save()
            return redirect('inventory:get_motor_home_details', id=motor_home.id)
        else:
            context = {
                'motor_home': motor_home,
                'form': form
            }
            return render(request, 'inventory/update.html', context)

@ensure_csrf_cookie
@require_http_methods(['DELETE'])
def delete_motor_home(request, id):
    if request.method == 'DELETE':
        try:
            motor_home = get_object_or_404(MotorHome, id=id)
            if motor_home is None:
                return JsonResponse({'message': 'Motor home not found'}, status=404)
            motor_home.delete()
            return JsonResponse({'message': 'Deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

def home(request):
    return render(request, 'inventory/dashboard.html')
