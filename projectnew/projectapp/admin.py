from django.contrib import admin
from . import models
# Register your models here.
class Student_Admin(admin.ModelAdmin):
    list_display=['name','rollno','telugu','hindi','english','maths','science','social','total','gpa','per']
admin.site.register(models.Student_Info,Student_Admin)
