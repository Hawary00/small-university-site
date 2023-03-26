from rest_framework import permissions
from django.contrib.auth.models import Group

from .models import *




#.has_permission(self, request, view)


class studentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(id=request.user.id)
        # group=user.groups.get(name='student_group')
        # user.user_permissions.set(group.permissions.all())
        if request.method == 'GET':
            return user.user_permissions.filter(codename="view_Student").exists()
        if request.method == 'POST':
            return user.user_permissions.filter(codename="add_Student").exists()
        if request.method == 'DELETE':
            return user.user_permissions.filter(codename="delete_Student").exists()
        if request.method == 'PATCH' or request.method == 'PUT':
            return user.user_permissions.filter(codename="change_Student").exists()
        

class doctorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(id=request.user.id)

        if request.method == 'GET':
            print(user.user_permissions.filter(
                codename="view_doctor").exists())
            return user.user_permissions.filter(codename="view_doctor").exists()
        if request.method == 'POST':
            return user.user_permissions.filter(codename="add_doctor").exists()
        if request.method == 'DELETE':
            return user.user_permissions.filter(codename="delete_doctor").exists()
        if request.method == 'PATCH' or request.method == 'PUT':
            return user.user_permissions.filter(codename="change_doctor").exists()
        

class coursesPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(id=request.user.id)

        if request.method == 'GET':
            print(user.user_permissions.filter(
                codename="view_courses").exists())
            return user.user_permissions.filter(codename="view_courses").exists()
        if request.method == 'POST':
            return user.user_permissions.filter(codename="add_courses").exists()
        if request.method == 'DELETE':
            return user.user_permissions.filter(codename="delete_courses").exists()
        if request.method == 'PATCH' or request.method == 'PUT':
            return user.user_permissions.filter(codename="change_courses").exists()        