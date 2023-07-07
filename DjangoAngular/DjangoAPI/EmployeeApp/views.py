import urllib.request
from urllib import request
from anyio import sleep

from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from EmployeeApp.models import Questions
from EmployeeApp.serializers import QuestionSerializer



# Create your views here.    
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
            id = questions_serializer.data['QuestionID']
            print(id)
            while chkDB(id) == 'none':
                sleep(1)
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


# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['uploadedFile']
#     file_name = default_storage.save(file.name,file)

#     return JsonResponse(file_name,safe=False)

@csrf_exempt
def chkDB(id):
    items = Questions.objects.get(QuestionID=id)
    return str(items.Response)