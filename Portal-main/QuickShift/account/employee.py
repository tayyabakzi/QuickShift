from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    Emp_Id = models.IntegerField()
    Name = models.CharField(max_length=50)
    Scheduling = models.CharField(max_length=50)
    Department = models.CharField(max_length=100)
    Team = models.CharField(max_length=50)
    Manager_Name = models.CharField(max_length=50)
    Manager_Id = models.IntegerField()
    Email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)



    def __str__(self):
        return self.Name