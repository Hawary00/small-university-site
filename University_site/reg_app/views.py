from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
#from reg_app import Serializers
from .Serializers import *
from rest_framework import viewsets
from knox.models import AuthToken
from rest_framework import generics, permissions
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.views.decorators.csrf import csrf_exempt
from .permissions import *
# Create your views here.
#from django.contrib.auth.models import User

#When you have a custom Django User model make sure you are importing it correctly in files that initiate User
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterAPI(generics.GenericAPIView):
    # queryset = User.objects.all(), Department.objects.all()
    serializer_class = Register_Serializer
    permission_classes =  (permissions.AllowAny,)
# PK IS NOT
    def post(self, request, *args, **kwargs):
        department=Department.objects.get(id=request.data['department00'])
        user_instance=User(department00=department)
        serializer = self.get_serializer(user_instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.validate(data=request.data)
        user = serializer.save()
    
        # print(user.set_password(request.data['password']))
        # print(serial`izer.data)
        return Response({
        "user" : serializer.data,
        "token" : AuthToken.objects.create(user)[1]
        })
    
        
    # def  get(self,request):
    #     s1 = User.objects.all()
    #     s2 = Rigister_Serializer(s1, many=True)
    #     return Response(s2.data)
    

class loginAPI(KnoxLoginView):
     permission_classes =  (permissions.AllowAny,)
     def post(self, request, format=None):
         serializer = AuthTokenSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         user = serializer.validated_data['user']
         login(request, user)
         return super(loginAPI, self).post(request, format=None)


class doc_view1(APIView) :
    
    def  get(self,request):
        s1 = doctor.objects.all()
        s2 = json_doctor_Serializers(s1, many=True)
        return Response(s2.data)
    def post(self,request):
        return Response({})

class doc_view(viewsets.ModelViewSet):
    queryset = doctor.objects
    serializer_class = json_doctor_Serializers
    permission_classes=(permissions.IsAuthenticated,doctorPermission,)
    def get_queryset(self): 
        id = self.request.user.id
        # what = User.role
        # role ==
        is_student = Student.objects.filter(user=id)
        print("is student", is_student)
        # id user
        is_doctor = doctor.objects.filter()
        print("is doctor", is_doctor)

        print("if statement")
        if is_student.exists():
            print(is_doctor)
            # print("AAAAAAAAA")
            # doctors = is_doctor.get()
            # print("fffffff")
            # doctor_name = doctors.doc_Name

            # doctor_dep = is_doctor.doctor_dep
            # print("zz")
            # print(doctor_name)
            # print("fffffff")
            
            
            # doc_view_dep = Department.objects.get()
            # docc = doc_view_dep.doc_dep.all()
        return is_doctor
    # self.queryset.filter(id=doctor_name.id), self.queryset.filter(id=doctor_dep.id)
   
        

        # id = self.request.user.id
        # is_doctor = doctor.objects.filter(user=id)
        # if self.request.user.is_doctor.exists():
        #     return User.objects.filter()
        # return User.objects.filter(id=self.request.user.id)
        
        






class Student_view(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = json_student_Serializers    
    permission_classes=(permissions.IsAuthenticated,studentPermission,)

    # def get_queryset(self):
    #     is_student = Student.objects.filter(id)
    #     if is_student:
    #     Student.objects.filter(id=id)
    #     qs = super().get_queryset()    
    #     return qs.filter(id=id)

    def get_queryset(self):

        id = self.request.user.id
        is_student = Student.objects.filter(user=id)
        if self.request.user.is_student.exists():
            return User.objects.filter()
        return User.objects.filter(id=self.request.user.id)
    
        
class courses_view(viewsets.ModelViewSet):
    queryset = courses.objects
    serializer_class = json_courses_Serializers  
    permission_classes=(coursesPermission,) 

    def get_queryset(self):
        id = self.request.user.id
        is_student = Student.objects.filter(user=id)
        if is_student.exists():
            student = is_student.get()
            courses = student.students_in_course.all()
        return courses    
    # courses.objects.filter(courses__studsent_course=id)

class Department_view(viewsets.ModelViewSet):
    queryset = Department.objects
    serializer_class = json_Department_Serializers
    permission_classes=[permissions.IsAuthenticated] 
    def get_queryset(self):
        id = self.request.user.id
        is_student = Student.objects.filter(user=id)
        # print("eeaereriiiiiiiiiiire")
        if is_student.exists():
            student = is_student.get()
            department = student.department
            print(department)
            return self.queryset.filter(id=department.id)
        