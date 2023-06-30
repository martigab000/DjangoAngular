import urllib.request
from urllib import request
from anyio import sleep

from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from EmployeeApp.models import Departments, Employees,Questions
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer, QuestionSerializer



# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
    
@csrf_exempt
def questionApi(request, id=0):
    if request.method=='GET':
        questions = Questions.objects.all()
        
        questions_serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(questions_serializer.data, safe=False)

    elif request.method=='POST':
        questions_data=JSONParser().parse(request)
        questions_serializer = QuestionSerializer(data=questions_data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            # sleep(5)
            # chkDB()
            return JsonResponse("Added Successfully!!" , safe=False)
        print(questions_serializer.errors)
        return JsonResponse("Failed to Add.",safe=False) 
    
    elif request.method=='PUT':
        questions_data = JSONParser().parse(request)
        questions=Questions.objects.get(QuestionID=questions_data['QuestionID'])
        questions_serializer=QuestionSerializer(questions,data=questions_data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        questions=Questions.objects.get(QuestionID=id)
        questions.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)

# @csrf_exempt
# def chkDB():
#     items = Questions.objects.db.
#     print(items.Input)
#     return