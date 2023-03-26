from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(doctor)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(courses)

