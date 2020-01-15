from django import forms
from . import models
class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student_Info
        exclude=['total','gpa','per']

class Delete(forms.Form):
    name=forms.CharField(max_length=30)
