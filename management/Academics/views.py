from __future__ import unicode_literals

from django.shortcuts import render
from Academics.models import *
from Academics.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

def academicsapp(request):
	return render(request,'academicsapp.html')
# def add_course(request):
# 	if request.method == 'POST':
# 		forms = CourseForm(request.POST,request.FILES)
# 		print (request.POST)
# 		if forms.is_valid():
# 			forms.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		forms = CourseForm()
# 	context_dict = {'forms':forms}
# 	return render (request,'form.html',context_dict)
def add_course(request):
    if request.method == 'POST':
        print (request.POST,'=====')
        Course.objects.create(
            Course_name= request.POST['course_name'],
            Description=request.POST['description'],
            Code=request.POST['code'],
            Minimum_attendance_in_percent=request.POST['minimum_attendance_in_percent'],
            Total_Working_Days=request.POST['total_working_days'])
        return HttpResponseRedirect('/course')
    else:
        forms = CourseForm()
        context_dict = {'forms':forms}
        return render (request,'courseform.html',context_dict)

def add_batch(request):
	if request.method == 'POST':
		forms = BatchForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = BatchForm()
	context_dict = {'forms':forms}
	return render (request,'addbatchform.html',context_dict)

def add_subject(request):
    if request.method == 'POST':
        Subject.objects.create(
            Subject_name= request.POST['subject_name'],
            Subject_code=request.POST['subject_code'],
            Subject_description=request.POST['subject_description'])
        return HttpResponseRedirect('/subject')
    else:
        forms = SubjectForm()
        context_dict = {'forms':forms}
        return render (request,'subjectform.html',context_dict)

# def add_subject(request):
# 	if request.method == 'POST':
#         Subject.objects.create(
#             Subject_name= request.POST['subject_name'],
#             Subject_code=request.POST['subject_code'],
#             Subject_description=request.POST['subject_description'])
#         return HttpResponseRedirect('/subject')
# 		# forms = SubjectForm(request.POST,request.FILES)
# 		# print (request.POST)
# 		# if forms.is_valid():
# 		# 	forms.save()
# 		# 	return HttpResponseRedirect('/')
# 	else:
# 		forms = SubjectForm()
# 	context_dict = {'forms':forms}
# 	return render (request,'subjectform.html',context_dict)

def add_exam(request):
	if request.method == 'POST':
		forms = ExamForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = ExamForm()
	context_dict = {'forms':forms}
	return render (request,'addexamform.html',context_dict)

def add_assignment(request):
	if request.method == 'POST':
		forms = AssignmentForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = AssignmentForm()
	context_dict = {'forms':forms}
	return render (request,'addassignmentform.html',context_dict)

def add_notes(request):
	if request.method == 'POST':
		forms = NotesForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = NotesForm()
	context_dict = {'forms':forms}
	return render (request,'addnotesform.html',context_dict)

# def add_certificate(request):
# 	if request.method == 'POST':
# 		forms = CertificatesForm(request.POST,request.FILES)
# 		print (request.POST)
# 		if forms.is_valid():
# 			forms.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		forms = CertificatesForm()
# 	context_dict = {'forms':forms}
# 	return render (request,'form.html',context_dict)

def add_certificate(request):
    if request.method == 'POST':
        Certificates.objects.create(
            Certificate_type= request.POST['Certificate_type'])
        return HttpResponseRedirect('/certificates')
    else:
        forms = CertificatesForm()
        context_dict = {'forms':forms}
        return render (request,'certificateform.html',context_dict)

def add_alumni(request):
	if request.method == 'POST':
		forms = AlumniForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = AlumniForm()
	context_dict = {'forms':forms}
	return render (request,'form.html',context_dict)

#####################################################################################################################

def getCourse(request):
    query =Course.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Course_name']= q.Course_name
        temp_dict['Description']= q.Description
        temp_dict['Code']= q.Code
        temp_dict['Minimum_attendance_in_percent']= q.Minimum_attendance_in_percent
        temp_dict['Total_Working_Days']= q.Total_Working_Days

        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'course.html',context_dict)



def getBatch(request):
    query =Batch.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Course_name']= q.Course_name
        temp_dict['Batch_name']= q.Batch_name
        temp_dict['Start_date']= q.Start_date
        temp_dict['End_Date']= q.End_Date
        temp_dict['Max_no_of_student']= q.Max_no_of_student


        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'batch.html',context_dict)



def getSubject(request):
    query =Subject.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Subject_name']= q.Subject_name
        temp_dict['Subject_code']= q.Subject_code
        temp_dict['Description']= q.Subject_description

        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'subject.html',context_dict)



def getExam(request):
    query =Exam.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Term']= q.Term
        temp_dict['Exam']= q.Exam_Name
        temp_dict['Subject_code']= q.Subject_code
        temp_dict['Student_Unique_Id']= q.Student_Unique_Id
        temp_dict['Full_marks']= q.Full_marks
        temp_dict['Pass_marks']= q.Pass_marks
        temp_dict['Marks_obtained']= q.Marks_obtained

        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'exam.html',context_dict)



def getAssignment(request):
    query =Assignment.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Assignment_Title']= q.Assignment_Title
        temp_dict['Assignment_Description']= q.Assignment_Description
        temp_dict['Course_name']= q.Course_name
        temp_dict['Batch_name']= q.Batch_name
        temp_dict['Subject_code']= q.Subject_code
        temp_dict['Date_Of_Submission']= q.Date_Of_Submission

        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'assignment.html',context_dict)



def getNotes(request):
    query =Notes.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Notes_Title']= q.Notes_Title
        temp_dict['Notes_Description']= q.Notes_Description
        temp_dict['Course_name']= q.Course_name
        temp_dict['Batch_name']= q.Batch_name
        temp_dict['Subject_code']= q.Subject_code
        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'notes.html',context_dict)



def getCertificate(request):
    query =Certificates.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Certificate_type']= q.Certificate_type

        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'certificate.html',context_dict)



def getAlumni(request):
    # query =Alumni.objects.all()
    # type_list = []
    # for q in query:
    #     temp_dict = {}
    #     temp_dict['EventType']= q.EventType
    #
    #     type_list.append(temp_dict)
    #
    # context_dict = {'query':type_list}
    #return render(request,'type.html',context_dict)
    return render(request,'alumni.html')




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class CourseListAPI(APIView):
	def get(self,request,format=None):
		aca = Course.objects.all()
		serializer = CourseSerializer(aca,many=True)
		return Response(serializer.data)

class BatchListAPI(APIView):
	def get(self,request,format=None):
		aca = Batch.objects.all()
		serializer = BatchSerializer(aca,many=True)
		return Response(serializer.data)

class SubjectListAPI(APIView):
	def get(self,request,format=None):
		aca = Subject.objects.all()
		serializer = SubjectSerializer(aca,many=True)
		return Response(serializer.data)
