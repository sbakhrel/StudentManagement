from __future__ import unicode_literals

from django.shortcuts import render
from Hostel.models import *
from Hostel.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

def hostelapp(request):
	return render(request,'hostelapp.html')
def Hostel_Detail(request):
    query =Hostel_Details.objects.all()
    hostel_detail_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Hostel_type']= q.Hostel_type
        temp_dict['Hostel_Name']=q.Hostel_Name
        hostel_detail_list.append(temp_dict)
    context_dict = {'query':hostel_detail_list}
    return render(request,'hosteldetail.html',context_dict)

def add_hostel_details(request):
    if request.method == 'POST':
        Hostel_Details.objects.create(
            Hostel_type= request.POST['hostel_type'],
            Hostel_Name=request.POST['hostel_name'])
        return HttpResponseRedirect('/hosteldetails')
    else:
        forms = Hostel_DetailsForm()
        context_dict = {'forms':forms}
        return render (request,'hostelform.html',context_dict)

# def add_hostel_details(request):
# 	if request.method == 'POST':
# 		forms = Hostel_DetailsForm(request.POST,request.FILES)
# 		print (request.POST)
# 		if forms.is_valid():
# 			forms.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		forms = Hostel_DetailsForm()
# 	context_dict = {'forms':forms}
# 	return render (request,'form.html',context_dict)

def getHostelRoom(request):
    query = Hostel_Room.objects.all()
    hostel_room_list = []
    for q in query:
        temp_dict = {}

        temp_dict['Hostel_Name']=q.Hostel_Name
        temp_dict['Floor_Name_or_No']= q.Floor_Name_or_No
        temp_dict['Room_No']= q.Room_No
        temp_dict['No_Of_Beds']= q.No_Of_Beds
        temp_dict['Amount']= q.Amount
        hostel_room_list.append(temp_dict)
    context_dict = {'query':hostel_room_list}
    return render(request,'hostelroom.html',context_dict)

def add_hostel_room(request):
	if request.method == 'POST':
		forms = Hostel_RoomForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = Hostel_RoomForm()
	context_dict = {'forms':forms}
	return render (request,'hostelroomaddform.html',context_dict)

def HostelRegister(request):
    query =Hostel_Register.objects.all()
    hostel_detail_list = []
    for q in query:
        temp_dict = {}
        temp_dict['User_type']= q.User_type
        temp_dict['Name']=q.Name
        temp_dict['In_out']= q.In_out
        temp_dict['Date']=q.Date
        temp_dict['Time']= q.Time

        hostel_detail_list.append(temp_dict)
    context_dict = {'query':hostel_detail_list}
    return render(request,'hostelregister.html',context_dict)


def add_hostel_regester(request):
    if request.method == 'POST':
        Hostel_Register.objects.create(
            User_type= request.POST['usertype'],
            Name=request.POST['name'],
            In_out=request.POST['in_out'],
            Date=request.POST['date'],
            Time=request.POST['time'])
        return HttpResponseRedirect('/hostelregister')
    else:
        forms = Hostel_RegisterForm()
        context_dict = {'forms':forms}
        return render (request,'hostelregistrationform.html',context_dict)


def HostelAllocation(request):
    query =Hostel_Allocation.objects.all()
    hostel_detail_list = []
    for q in query:
        temp_dict = {}
        temp_dict['User_type']= q.User_type
        temp_dict['Hostel_Name']=q.Hostel_Name
        temp_dict['Room_No']= q.Room_No
        temp_dict['Hostel_Regd_Date']=q.Hostel_Regd_Date
        temp_dict['Vacating_Date']= q.Vacating_Date

        hostel_detail_list.append(temp_dict)
    context_dict = {'query':hostel_detail_list}
    return render(request,'hostelallocation.html',context_dict)

def add_hostelallocation(request):
	if request.method == 'POST':
		forms = Hostel_AllocationForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = Hostel_AllocationForm()
	context_dict = {'forms':forms}
	return render (request,'hostelallocationform.html',context_dict)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class HostelDetailList(APIView):
	def get(self,request,format=None):
		hostel = Hostel_Details.objects.all()
		serializer = HostelDetailSerializer(hostel,many=True)
		return Response(serializer.data)
class HostelRoomList(APIView):
	def get(self,request,format=None):
		hostel = Hostel_Room.objects.all()
		serializer = HostelRoomSerializer(hostel,many=True)
		return Response(serializer.data)
class HostelRegList(APIView):
	def get(self,request,format=None):
		hostel = Hostel_Register.objects.all()
		serializer = HostelRegisterSerializer(hostel,many=True)
		return Response(serializer.data)
