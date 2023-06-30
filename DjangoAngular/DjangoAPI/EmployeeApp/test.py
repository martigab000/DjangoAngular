# import urllib.request
# from urllib import request
# from anyio import sleep

# from django.core.files.storage import default_storage
# from django.http.response import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

from models import Questions
# from serializers import DepartmentSerializer, EmployeeSerializer, QuestionSerializer

items = Questions.from_db('db.sqlite3')
print(items)