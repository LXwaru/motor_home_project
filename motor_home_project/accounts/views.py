from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UpdateEmployeeForm, CreateEmployeeForm
from .models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET', 'POST'])
def create_employee(request):
    if request.method == 'GET':
        form = CreateEmployeeForm()
        return render(request, 'accounts/create_employee.html', {'form': form})
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/list_employees.html', {'form': form})
    return render(request, 'accounts/list_employees.html')

@login_required
@require_http_methods(['GET'])
def list_employees(request):
    active_employees = Employee.objects.filter(is_active=True)
    inactive_employees = Employee.objects.filter(is_active=False)
    context = {
        'active_employees': active_employees,
        'inactive_employees': inactive_employees
    }
    return render(request, 'accounts/list_employees.html', context)

@login_required
@require_http_methods(['GET'])
def profile_employee(request, id):
    if request.method == 'GET':
        employee = Employee.objects.get(id=id)
        context = {
            'employee': employee
        }
    return render(request, 'accounts/profile_employee.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'GET':
        form = UpdateEmployeeForm(instance=employee)
        context = { 
            'form': form,
            'employee': employee
        }
        return render(request, 'accounts/update_employee.html', context)
    if request.method == 'POST':
        form = UpdateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('accounts:list_employees')
    return render(request, 'accounts/update_employee.html', {'form': form, 'employee': employee})

@login_required
@require_http_methods(['POST'])
def deactivate_employee(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=id)
        employee.is_active = False
        employee.save()
        return redirect('accounts:profile_employee', id=id)

@login_required
@require_http_methods(['POST'])
def activate_employee(request, id): 
    employee = get_object_or_404(Employee, id=id)
    employee.is_active = True
    employee.save()
    return redirect('accounts:profile_employee', id=id)

@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:list_employees')
        return render(request, 'accounts/login.html', {'form': form})

@require_http_methods(['GET'])
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')