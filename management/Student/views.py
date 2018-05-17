from __future__ import unicode_literals

from django.shortcuts import render
from Student.models import *
from Student.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import Http404


@login_required(login_url='/admin/')

def home(request):
	return render(request,'home.html')

def studentapp(request):
	return render(request,'studentapp.html')

def student_grade(request):
    query =Student_Grade.objects.all()
    student_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Grade']= q.Grade
        student_list.append(temp_dict)
    context_dict = {'query':student_list}
    return render(request,'grade.html',context_dict)

def add_grade(request):
    if request.method == 'POST':
        Student_Grade.objects.create(
            Grade=request.POST['grade_name'])
        return HttpResponseRedirect('/grade')
    else:
        forms = GradeForm()
        context_dict = {'forms':forms}
        return render (request,'addgrade.html',context_dict)

def student_faculty(request):
    query =Student_Faculty.objects.all()
    student_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Faculty']= q.Faculty
        student_list.append(temp_dict)
    context_dict = {'query':student_list}
    return render(request,'faculty.html',context_dict)

# def add_faculty(request):
# 	if request.method == 'POST':
# 		forms = FacultyForm(request.POST,request.FILES)
# 		print (request.POST)
# 		if forms.is_valid():
# 			forms.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		forms = FacultyForm()
# 	context_dict = {'forms':forms}
# 	return render (request,'form.html',context_dict)

def add_faculty(request):
    if request.method == 'POST':
        Student_Faculty.objects.create(
            Faculty=request.POST['faculty'])
        return HttpResponseRedirect('/faculty')
    else:
        forms = FacultyForm()
        context_dict = {'forms':forms}
        return render (request,'facultyform.html',context_dict)

def student_list(request):
    query =Student_Admission.objects.all()
    student_list = []
    for q in query:
        temp_dict = {}
        temp_dict['First_Name']= q.First_Name
        temp_dict['Middle_Name']= q.Middle_Name
        temp_dict['Family_Name']= q.Family_Name
        temp_dict['Gender']= q.Gender
        student_list.append(temp_dict)
    context_dict = {'query':student_list}
    return render(request,'student.html',context_dict)

def add_student(request):
	if request.method == 'POST':
		forms = StudentForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = StudentForm()
	context_dict = {'forms':forms}
	return render (request,'addstudentform.html',context_dict)


class GradeList(APIView):
	def get(self,request,format=None):
		grade = Student_Grade.objects.all()
		serializer = GradeSerializer(grade,many=True)
		return Response(serializer.data)

class FacultyList(APIView):
	def get(self,request,format=None):
		faculty = Student_Faculty.objects.all()
		serializer = FacultySerializer(faculty,many=True)
		return Response(serializer.data)

class StudentList(APIView):
	def get(self,request,format=None):
		student = Student_Admission.objects.all()
		serializer = StudentSerializer(student,many=True)
		return Response(serializer.data)
