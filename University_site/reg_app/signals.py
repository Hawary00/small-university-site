
from .models import *
from django.dispatch import receiver
# from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.contrib.auth.models import Group



# @receiver(post_save, sender=User)
# def create_group(sender, instance, created=True, **kwargs):
#     user = User.objects.get(id.user.id)
#     group=user.groups.get(name='student_group')
#     user.user_permissions.set(group.permissions.all())



@receiver(post_save, sender=User)
def create_profile(sender, instance, created=False, **kwargs):
    # user = User.objects.get(id.User.id)
    if created:
        if not instance.is_superuser:
            instance.set_password(instance.password)
            instance.save()
        role=instance.role
        if role =='student': 
            student=Student.objects.create(user=instance, student_Name=instance.username, department=instance.department00)
            my_group = Group.objects.get(name='student_group')
            instance.user_permissions.set(my_group.permissions.all())
            instance.groups.add(my_group)

        elif role == 'doctor':
            print(instance.phone)  
            doctor_obj = doctor.objects.create(user=instance, doc_Name=instance.username, doctor_dep=instance.department00)
            my_group = Group.objects.get(name='doctor_group')
            instance.user_permissions.set(my_group.permissions.all())
            instance.groups.add(my_group)




 
