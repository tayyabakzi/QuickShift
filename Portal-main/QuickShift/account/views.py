from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .forms import EmployeeForm
from .models import Employee
import csv, io

# Create your views here.
def login(request):
    return render(request, 'login.html')

def HR_Profile(request):
    return  render(request, 'hrProfile.html')

def employeeProfile(request):
    return  render(request, 'employeeProfile.html')

def schedule(request):
    return  render(request, 'schedule.html')
def timeslot(request):
    return  render(request, 'timeslot.html')
def changeSchedule(request):
    return  render(request, 'changeSchedule.html')

def calander(request):
    data = Employee.objects.all()
    return  render(request, 'calander.html', {"employees":data})

def employeeDetails(request):
    form = EmployeeForm()  # Initialize the form variable
    if request.method == "POST":
        if 'file' in request.FILES:
            # handle CSV file upload
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a CSV file.')
            else:
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    emp_data = {
                        "Emp_Id": column[0],
                        "Name": column[1],
                        "Scheduling": column[2],
                        "Department": column[3],
                        "Team": column[4],
                        "Manager_Name": column[5],
                        "Manager_Id": column[6],
                        "Email": column[7],
                    }
                    # Create a new Employee object or update the existing one
                    employee, created = Employee.objects.update_or_create(
                        Emp_Id=emp_data["Emp_Id"],
                        defaults=emp_data
                    )
                    if created:
                        # Save the newly created object
                        messages.success(request, f'Employee {employee.Name} ({employee.Emp_Id}) created successfully.')
                    else:
                        # Save the updated object
                        messages.success(request, f'Employee {employee.Name} ({employee.Emp_Id}) updated successfully.')
        else:
            # handle manual employee form submission
            form = EmployeeForm(request.POST)
            if form.is_valid():
                employee = form.save(commit=False)
                employee.save()
                messages.success(request, f'Employee {employee.Name} ({employee.Emp_Id}) saved successfully.')
                return redirect("organization")
            else:
                messages.error(request, 'Form data is not valid. Please correct the errors.')
    template = "employeeDetails.html"
    data = Employee.objects.all()
    prompt = {
        'order': 'Order of the CSV should be Emp_Id, Name, Scheduling, Department, Team, Manager_Name, Manager_Id, Email',
        'employees': data
    }
    return render(request, template, {"form": form, "prompt": prompt})

def companyDetails(request):
    return  render(request, 'companyDetails.html')

def expenseDetails(request):
    return  render(request, 'expenseDetails.html')

def organization(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        employee_id = request.POST.get('id')
        if 'edit_employee' in request.POST:
            employee = Employee.objects.get(id=employee_id)
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
        elif 'delete_employee' in request.POST:
            Employee.objects.filter(id=employee_id).delete()
        return redirect("organization")
    else:
        form = EmployeeForm()
    return render(request, 'organization.html', {"employees": employees, "form": form})