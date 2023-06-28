from rest_framework import serializers

from EmployeeApp.models import Departments, Employees, Questions


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions 
        fields = ('QuestionID',
                  'Input',
                  'Response',
                  'Date')