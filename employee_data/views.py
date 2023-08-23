from django.shortcuts import render
from employee_data.models import Employee
from employee_data.forms import EmployeeForm
from employee_data.forms import EmployeeFormset
from django.http import JsonResponse


def employee_data(request):
    return render(request, "employee_data.html",{})
# Create your views here.

def homepage(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, 'homepage.html', context)

def employee(request, id):
    employee =Employee.objects.get(id=id)
    context = {
        'employee': employee
    }
    return render(request, 'employee.html',context)

def add_data(request):

    context = {
        'form' : EmployeeForm()
    }
    if request.method == 'POST':
        pass
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image =  form.instance
            context = {
                'form' : form
            }
            return render(request, 'add_data.html',context)
    else:
        return render(request,'add_data.html', {'form' : EmployeeForm()})

