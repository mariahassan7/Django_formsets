from django.shortcuts import render, redirect
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

# def add_data(request):

#     context = {
#         'form' : EmployeeForm()
#     }
#     if request.method == 'POST':
#         pass
#         form = EmployeeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             image =  form.instance
#             context = {
#                 'form' : form
#             }
#             return render(request, 'add_data.html',context)
#     else:
#         return render(request,'add_data.html', {'form' : EmployeeForm()})

def add_data(request):
    if request.method =="GET":
        employee_form_set = EmployeeFormset(request.GET or None)
    if request.method == "POST":
        print("here")
        employee_form_set = EmployeeFormset(request.POST)
        if employee_form_set.is_valid():
            for one_form in employee_form_set:
                employee_name = one_form.cleaned_data.get('name')
                employee_designation = one_form.cleaned_data.get('designation')
                employee_bio = one_form.cleaned_data.get('bio')
                employee_skills = one_form.cleaned_data.get('skills')
                if employee_name:
                    save_employee_data = Employee(name=employee_name, designation=employee_designation, bio=employee_bio, skills=employee_skills)
                    save_employee_data.save()              
    return render(request,'add_data.html', {'formset' : employee_form_set })
    