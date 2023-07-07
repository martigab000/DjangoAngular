from rest_framework import serializers

from EmployeeApp.models import Questions

        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions 
        fields = ('QuestionID',
                  'Input',
                  'Response',
                  'Date')