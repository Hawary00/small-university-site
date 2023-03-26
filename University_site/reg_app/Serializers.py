#from University_site.reg_app.models import Student
from .models import *
from rest_framework import serializers
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.contrib.auth import get_user_model
User = get_user_model()

#User Registration API using Django Rest Framework

# user Serializer
# not use i dont know why i create it 
# class user_serializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username", "email")





class json_Department_Serializers(serializers.ModelSerializer):
    class Meta :
        model = Department
        fields=('name',)
   
        



# Register Serializer
class Register_Serializer(serializers.ModelSerializer):
    # Department0 = json_Department_Serializers()
    class Meta:
        model = User
        fields = ('id', 'username','email', 'password', 'role', 'phone') #,'Department0'
        extra_kwargs = {'password':{'write_only': True}}
       
    def validate(self,data):
        # if  not validate_email(data['email']):
        #     raise serializers.ValidationError({'detail':'enter a valid mail'})
        if not data['role']:
            raise serializers.ValidationError({'detail':'chose a valid role'})
        return data

        # elif phonenumbers.parse(data):
        #     raise serializers.ValidationError({{'details':'enter yor phone num'}})
        # validate_email()    
        # 
        # # def create(self, ):
    #     department
    
    # return 
# validate_email(data)



#############################################################




# class register_srializer(serializers.ModelSerializer):
#     register_extendeds = Task_extendedSerializer()
#     class Meta:
#         model = Task
#         fields = ('id', 'title', 'completed', 'task_extendeds')



    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
    #     return user
#######################################################################


class json_doctor_Serializers(serializers.ModelSerializer):
    doctor_dep = json_Department_Serializers()
    class Meta :
        model = doctor
        fields =('doc_Name','doctor_dep')
     
        


class json_student_Serializers(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields =('department',)

class json_courses_Serializers(serializers.ModelSerializer):
    class Meta :
        model = courses
        fields =('course_Name',)

