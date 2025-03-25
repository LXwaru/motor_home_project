from django.shortcuts import render
from .models import MotorHome, Model
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404


@require_http_methods(['GET'])
def get_inventory(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        motor_homes = MotorHome.objects.all()
        motor_homes_list = list(motor_homes.values(
            'id', 
            'vin', 
            'year', 
            'mileage', 
            'condition',
            'model_id',
            'color',
            'ticket_price', 
            'image',
            'is_new',
            'for_sale',
            'is_sold',
            'sold_date'
        ))
        context = {
            'motor_homes': motor_homes_list
        }
        
        return JsonResponse(context)

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
        motor_home_details = {
            'id': motor_home.id,
            'vin': motor_home.vin,
            'year': motor_home.year,
            'mileage': motor_home.mileage,
            'condition': motor_home.condition,
            'model_id': motor_home.model_id.id,
            'color': motor_home.color,
            'ticket_price': motor_home.ticket_price,
            'image': motor_home.image.url if motor_home.image else None,
        }
        return JsonResponse(motor_home_details)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@ensure_csrf_cookie
@require_http_methods(['PUT'])
def update_motor_home(request, id):
    if request.method == 'PUT':
        try:
            content = json.loads(request.body)
            motor_home = get_object_or_404(MotorHome, id=id)
            for field, value in content.items():
                setattr(motor_home, field, value)
            motor_home.save()
            return JsonResponse({'message': 'Updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)


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
