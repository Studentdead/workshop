from django.urls import path
from django.contrib import admin
from .views import postStudent,postTeacher,getStudent,getTeacher,deleteTeacher,editStudent,getTeacherById,editTeacher,deleteStudent,getStudentById
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
app_name='core'
urlpatterns+=[
    path('add-student/',postStudent),
    path('add-teacher/',postTeacher),
    path('get-student/',getStudent),
    path('get-student/<id>',getStudentById),
    path('get-teacher/',getTeacher),
    path('get-teacher/<id>',getTeacherById),
    path('edit-student/<id>',editStudent),
    path('edit-teacher/<id>',editTeacher),
    path('delete-student/<id>',deleteStudent),
    path('delete-teacher/<id>',deleteTeacher)
]