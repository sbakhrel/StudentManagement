from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Vehicle(models.Model):
    type_choices=(
        ('Contract','Contract'),
        ('Ownership','Ownership')
    )
    Vehicle_Number=models.CharField(max_length=15)
    No_Of_Seats=models.DecimalField(max_digits=3, decimal_places=0)
    Maximum_allowed=models.DecimalField(max_digits=3,decimal_places=0)
    Vehicle_type=models.CharField(max_length=10,choices=type_choices)

    def __str__(self):
        return '%s'%(self.Vehicle_Number)


class Route(models.Model):
    Vehicle_Number=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    Route_code=models.CharField(max_length=20)
    Start_place=models.CharField(max_length=25)
    Stop_place=models.CharField(max_length=25)

    def __str__(self):
        return '%s'%(self.Route_code)

class Driver(models.Model):
    Vehicle_Number=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Permanent_Address=models.CharField(max_length=25)
    Present_Address=models.CharField(max_length=25)
    Date_of_birth=models.DateField()
    Phone=models.DecimalField(max_digits=10,decimal_places=0)
    License_Number=models.CharField(max_length=15)

    def __str__(self):
        return '%s'%(self.Name)

class Transport_Allocation(models.Model):
    pessenger_choices=(
    ('Student','Student'),
    ('Employee','Employee')
    )

    Route_code=models.ForeignKey(Route,on_delete=models.CASCADE)
    Destination=models.CharField(max_length=20)
    Type_of_Pessenge=models.CharField(max_length=10,choices=pessenger_choices)
    Frequency=models.DecimalField(max_digits=2,decimal_places=0)

    def __str__(self):
        return '%s'%(self.Route_code)
