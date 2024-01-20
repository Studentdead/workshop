from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer,TeacherSerializer
from .models import Student,Teacher

# Create your views here
@api_view(['POST'])
def postStudent(request):
   try:
        request_data=request.data
        serializer=StudentSerializer(data=request_data,many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Student Saved"})
   except Exception as e:
       return Response({"err":str(e)})
    
  
@api_view(['POST'])
def postTeacher(request):
    try:
        request_data=request.data
        serializer=TeacherSerializer(data=request_data,many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Teacher Saved"})
    except Exception as e:
        return Response({"err":str(e)})
    
@api_view(['GET'])
def getStudent(request):
    try:
        students=Student.objects.all()
        serialized_data=StudentSerializer(students,many=True)
        
        return Response(serialized_data.data)
                
    except Exception as e:
        return Response({"err":str(e)})

@api_view(['GET'])
def getTeacher(request):
    try:
        teachers=Teacher.objects.all()
        serialized_data=TeacherSerializer(teachers,many=True)
        return Response(serialized_data.data)
                    
    except Exception as e:
        return Response({"err":str(e)})

@api_view(['POST'])
def editStudent(request,id):
    try:
        student=Student.objects.get(id=id)
        serialized_data=TeacherSerializer(student,data=request.data,many=False,partial=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response({"Message:Updated succesfully"})
    except Exception as e:
        return Response({"err":str(e)})
        
        

@api_view(['POST'])
def editTeacher(request,id):
    try:
        student=Teacher.objects.get(id=id)
        serialized_data=TeacherSerializer(student,data=request.data,many=False,partial=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response({"Message:Updated succesfully"})
    except Exception as e:
        return Response({"err":str(e)})
        

@api_view(['GET'])
def deleteStudent(request,id):
    try:
        student = get_object_or_404(Student, id=id)
        student.delete()

        return Response({"message:Deleted Succesfully"})
    except Exception as e:
        return Response({"err":str(e)})

@api_view(['GET'])
def deleteTeacher(request,id):
    try:
        student = get_object_or_404(Teacher, id=id)

        student.delete()

        return Response({"message:Deleted Succesfully"})
    except Exception as e:
        return Response({"err":str(e)})
    
    

@api_view(['GET'])
def getStudentById(request,id):
    try:
        student=get_object_or_404(Student,id=id)
        serialized=StudentSerializer(student,many=False)
        return Response(serialized.data)
    except Exception as e:
        return Response({"err":str(e)})

@api_view(['GET'])
def getTeacherById(request,id):
    try:
        student=get_object_or_404(Teacher,id=id)
        serialized=StudentSerializer(student,many=False)
        return Response(serialized)
    except Exception as e:
        return Response({"err":str(e)})