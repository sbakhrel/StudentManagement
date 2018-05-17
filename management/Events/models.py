from __future__ import unicode_literals
from django.db import models

class Event_Type(models.Model):

    EventType=models.CharField(max_length=15)

    def __str__(self):
        return '%s'%(self.EventType)


class Event(models.Model):

    Event_Name=models.CharField(max_length=25)
    EventType=models.ForeignKey(Event_Type,on_delete=models.CASCADE)
    Description=models.TextField()
    Startdate=models.DateField()
    Enddate=models.DateField()
    Organizer=models.CharField(max_length=20)
    Remarks=models.TextField()

    def __str__(self):
        return '%s'%(self.Event_Name)
