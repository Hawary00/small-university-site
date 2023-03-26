from django.urls import path, include
from reg_app import views
from rest_framework import routers
from .views import *
from knox import views as knox_views


r = routers.DefaultRouter()
r.register('doctors',views.doc_view)
r.register('students',views.Student_view)
r.register('departments',views.Department_view)
r.register('courses',views.courses_view)

# r.register('courses',views.doc_view1.as_view())

# r2 = routers.DefaultRouter()
# r2.register('',views.Student_list1)

# r3 = routers.DefaultRouter()

# r4 = routers.DefaultRouter()


urlpatterns = [
    
     path('doc_list/',doc_view1.as_view() , name = 'doc_view'),
     path('', include(r.urls), name = 'api' ),
     path('api/register/', RegisterAPI.as_view(), name='register'),
     path('api/login/', loginAPI.as_view(), name='login'),
     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
     path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
     # path('api/doc_view1',views.doc_view1.as)
     # path('student_list1/', include(r2.urls), name = 'studentjson1' ),
     # path('courses_list1/', include(r3.urls), name = 'Json_doctor'),
     # path('Department_list1/', include(r4.urls), name = 'user_json'),
     
    
]

