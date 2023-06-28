from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length= 100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

class Questions(models.Model):
    QuestionID = models.AutoField(primary_key=True)
    Input = models.CharField(max_length=100)
    Response = models.CharField(max_length=100)
    Date = models.DateField()