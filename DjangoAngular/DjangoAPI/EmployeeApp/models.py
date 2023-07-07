from django.db import models

# Create your models here.

class Questions(models.Model):
    QuestionID = models.AutoField(primary_key=True)
    Input = models.CharField(max_length=1000)
    Response = models.CharField(max_length=1000)
    Date = models.DateField()