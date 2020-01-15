from django.db import models

# Create your models here.
class Student_Info(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    rollno=models.IntegerField()
    telugu=models.IntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    social=models.IntegerField()
    total=models.FloatField()
    gpa=models.FloatField()
    per=models.FloatField()
