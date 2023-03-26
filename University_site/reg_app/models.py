from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.paginator import Paginator

from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers
# Create your models here.

class Department(models.Model):
    departments = (('IT','IT'),('CS','CS'))
    name = models.CharField(max_length=20, choices=departments, default=None)
    def __str__(self):
        return self.name
    

class User(AbstractUser):
    roles = (('doctor','doctor'),('student','student'))
    role = models.CharField(max_length=200, choices=roles)
    department00 = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    phone = PhoneNumberField(max_length=20,unique=True)
    email=models.EmailField(unique=True)




# class Department(models.Model):
#     departments = (('IT','IT'),('CS','CS'))
#     Department = models.CharField(max_length=20, choices=departments, default='SOME STRING')
#     def __str__(self):
#         return self.Department  




class doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doc_Name = models.CharField(max_length = 20)   
    doctor_dep = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='doc_dep')

    def __str__(self):
        return self.doc_Name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_Name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, )
    
    


class courses(models.Model):
    course_Name = models.CharField(max_length=20)
    student_course = models.ManyToManyField(Student,related_name='students_in_course')
    doctor_courses = models.OneToOneField(doctor, on_delete=models.CASCADE)


   
    



    

    


