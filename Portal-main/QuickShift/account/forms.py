from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    Emp_Id = forms.IntegerField(label="employee ID")
    Name = forms.CharField(label="full name", max_length=50)
    Scheduling = forms.CharField(label="scheduling", max_length=50)
    Department = forms.CharField(label='department', max_length=100)
    Team = forms.CharField(label='team', max_length=50)
    Manager_Name = forms.CharField(label='manager name', max_length=50)
    Manager_Id = forms.IntegerField(label='manager ID')
    Email = forms.EmailField(label='email')

    class Meta:
        model = Employee
        exclude = ("user",)