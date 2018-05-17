from __future__ import unicode_literals

from django.shortcuts import render
from Transport.models import *
from Transport.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

def transportapp(request):
	return render(request,'transportapp.html')
def Vehicle_list(request):
    query =Vehicle.objects.all()
    vehicle_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Vehicle_Number']= q.Vehicle_Number
        temp_dict['No_Of_Seats']=q.No_Of_Seats
        temp_dict['Maximum_allowed']=q.Maximum_allowed
        temp_dict['Vehicle_type']=q.Vehicle_type
        vehicle_list.append(temp_dict)
    context_dict = {'query':vehicle_list}
    return render(request,'vehiclelist.html',context_dict)

def add_vehicle(request):
	if request.method == 'POST':
		forms = VehicleForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = VehicleForm()
	context_dict = {'forms':forms}
	return render (request,'addvechicleform.html',context_dict)


def Route_list(request):
    query =Route.objects.all()
    route_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Vehicle_Number']= q.Vehicle_Number
        temp_dict['Route_code']=q.Route_code
        temp_dict['Start_place']=q.Start_place
        temp_dict['Stop_place']=q.Stop_place
        route_list.append(temp_dict)
    context_dict = {'query':route_list}
    return render(request,'routelist.html',context_dict)


def add_route(request):
	if request.method == 'POST':
		forms =RouteForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = RouteForm()
	context_dict = {'forms':forms}
	return render (request,'addroute.html',context_dict)


def Driver_list(request):
    query =Driver.objects.all()
    driver_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Vehicle_Number']= q.Vehicle_Number
        temp_dict['Name']=q.Name
        temp_dict['Permanent_Address']=q.Permanent_Address
        temp_dict['Present_Address']=q.Present_Address
        temp_dict['Date_of_birth']=q.Date_of_birth
        temp_dict['Phone']=q.Phone
        temp_dict['License_Number']=q.License_Number
        driver_list.append(temp_dict)
    context_dict = {'query':driver_list}
    return render(request,'driverlist.html',context_dict)

# def add_driver(request):
# 	if request.method == 'POST':
# 		forms =DriverForm(request.POST,request.FILES)
# 		print (request.POST)
# 		if forms.is_valid():
# 			forms.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		forms = DriverForm()
# 	context_dict = {'forms':forms}
# 	return render (request,'form.html',context_dict)

def add_driver(request):
    if request.method == 'POST':
        Vehicle.objects.create(
            Vehicle_Number= request.POST['Vehicle_Number'],
            No_Of_Seats=request.POST['No_Of_Seats'],
            Maximum_allowed=request.POST['Maximum_allowed'],
            Vehicle_type=request.POST['Vehicle_type'])
        return HttpResponseRedirect('/')
    else:
        forms = DriverForm()
        context_dict = {'forms':forms}
        return render (request,'adddriver.html',context_dict)

def Transport_Allocation_list(request):
    query =Transport_Allocation.objects.all()
    ta_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Route_code']= q.Route_code
        temp_dict['Destination']=q.Destination
        temp_dict['Type_of_Pessenge']=q.Type_of_Pessenge
        temp_dict['Frequency']=q.Frequency
        ta_list.append(temp_dict)
    context_dict = {'query':ta_list}
    return render(request,'talist.html',context_dict)


def add_ta(request):
	if request.method == 'POST':
		forms =Transport_AllocationForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = Transport_AllocationForm()
	context_dict = {'forms':forms}
	return render (request,'driverallocationadd.html',context_dict)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class VehicleListAPI(APIView):
	def get(self,request,format=None):
		transport = Vehicle.objects.all()
		serializer = VehicleSerializer(transport,many=True)
		return Response(serializer.data)

class RouteListAPI(APIView):
	def get(self,request,format=None):
		transport = Route.objects.all()
		serializer = RouteSerializer(transport,many=True)
		return Response(serializer.data)
