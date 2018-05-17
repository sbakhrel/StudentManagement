from __future__ import unicode_literals

from django.shortcuts import render
from Events.models import *
from Events.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required


def eventsapp(request):
	return render(request,'eventsapp.html')
def getEventType(request):
    query =Event_Type.objects.all()
    type_list = []
    for q in query:
        temp_dict = {}
        temp_dict['EventType']= q.EventType
        type_list.append(temp_dict)

    context_dict = {'query':type_list}
    return render(request,'type.html',context_dict)

def add_eventtype(request):
    if request.method == 'POST':
        Event_Type.objects.create(
            EventType= request.POST['event_type'])
        return HttpResponseRedirect('/eventtype')
    else:
        forms = typeForm()
        context_dict = {'forms':forms}
        return render (request,'eventtypeform.html',context_dict)

def getEvent(request):
    query =Event.objects.all()
    event_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Event_Name']= q.Event_Name
        temp_dict['EventType']= q.EventType
        temp_dict['Description']= q.Description
        temp_dict['Startdate']= q.Startdate
        temp_dict['Enddate']= q.Enddate
        temp_dict['Organizer']= q.Organizer
        temp_dict['Remarks']= q.Remarks

        event_list.append(temp_dict)

    context_dict = {'query':event_list}
    return render(request,'event.html',context_dict)


def add_event(request):
    if request.method == 'POST':
        # event_name = request.POST['Event_Name']
        # print (event_name,'----')
        print (request.POST['event_name'])
        print(request.POST['event_type'])
        # Event.objects.create(
        #     Event_Name= request.POST['event_name'],
        #     EventType=request.POST['event_type'],
        #     Startdate=request.POST[''],
        #     Enddate=request.POST[''],
    # EventType=models.ForeignKey(Event_Type,on_delete=models.CASCADE)
    # Description=models.TextField()
    # Startdate=models.DateField()
    # Enddate=models.DateField()
    # Organizer=models.CharField(max_length=20)
    # Remarks=models.TextField()
    #         )
        # if forms.is_valid():
        #     forms.save()
        return HttpResponseRedirect('/')
    else:
        forms = EventForm()
    context_dict = {'forms':forms}
    return render (request,'eventform.html',context_dict)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class EventList(APIView):
	def get(self,request,format=None):
		event = Event_Type.objects.all()
		serializer = EventTypeSerializer(event,many=True)
		return Response(serializer.data)
