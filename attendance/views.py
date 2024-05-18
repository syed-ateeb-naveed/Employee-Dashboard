from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from .forms import LoginForm
from .models import *
from datetime import date, time
from .script import create_employee_login, create_attendance
# Create your views here.


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            dig_id = form.cleaned_data['emp_dig_id']
            password = form.cleaned_data['emp_password']
            print(EMPLOYEE_LOGIN.objects.all()) 
            user = EMPLOYEE_LOGIN.objects.filter(EMP_DIG_ID=dig_id).first()
            try:
                check_pass = check_password(password, user.EMP_PASSWORD)
            except:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login'})
            print(user)
            if user is not None:
                # Perform any additional authentication checks if needed
                return redirect('dashboard')
            else:
                # Return an 'invalid login' error message
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    total_employees = EMPLOYEE_LOGIN.objects.count()
    present_employees = 0
    employees_before_9 = 0
    present_employees_with_checkout = 0
    present_employees_with_checkout_before_345 = 0
    for check_in in EMP_ATTENDANCE_REC.objects.all():
        if check_in.EMP_CHECKIN_DATETIME.date() == date.today():
            present_employees = present_employees + 1
            if check_in.EMP_CHECKIN_DATETIME.time() < time(9, 0, 0):
                employees_before_9 = employees_before_9 + 1
            if check_in.EMP_CHECKOUT_DATETIME:
                present_employees_with_checkout = present_employees_with_checkout + 1
                if check_in.EMP_CHECKOUT_DATETIME.time() < time(15, 45, 0):
                    present_employees_with_checkout_before_345 = present_employees_with_checkout_before_345 + 1
    present_employees_with_checkout_after_345 = present_employees_with_checkout - present_employees_with_checkout_before_345
    present_employees_missing_checkout = present_employees - present_employees_with_checkout
    employees_after_9 = present_employees - employees_before_9
    absent_employees = total_employees - present_employees
    context = {
        'total_employees': total_employees,
        'present_employees': present_employees,
        'absent_employees': absent_employees,
        'employees_before_9': employees_before_9,
        'employees_after_9': employees_after_9,
        'present_employees_missing_checkout': present_employees_missing_checkout,
        'present_employees_with_checkout': present_employees_with_checkout,
        'present_employees_with_checkout_before_345': present_employees_with_checkout_before_345,
        'present_employees_with_checkout_after_345': present_employees_with_checkout_after_345,
    }
    return render(request, 'dashboard.html', context)

def create(request):
    create_employee_login()
    return redirect('dashboard')

def create2(request):
    create_attendance()
    return redirect('dashboard')