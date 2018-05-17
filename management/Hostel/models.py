from __future__ import unicode_literals
from django.db import models

class Hostel_Details(models.Model):
    type_choices=(
        ('Boys-Hostel','Boys-Hostel'),
        ('Girls-Hostel','Girls-Hostel')
    )

    Hostel_type=models.CharField(max_length=15,choices=type_choices)
    Hostel_Name=models.CharField(max_length=20)

    def __str__(self):
        return '%s'%(self.Hostel_Name)

class Hostel_Room(models.Model):

    #Hostel_type=models.ForeignKey(Hostel_Details,on_delete=models.CASCADE)
    Hostel_Name=models.ForeignKey(Hostel_Details,on_delete=models.CASCADE)
    Floor_Name_or_No=models.CharField(max_length=10)
    Room_No=models.DecimalField(max_digits=5,decimal_places=0)
    No_Of_Beds=models.DecimalField(max_digits=2,decimal_places=0)
    Amount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return '%s'%(self.Hostel_Name)

class Hostel_Register(models.Model):

    user_choices=(
    ('Employee','Employee'),
    ('Student','Student'),
    ('Visitor','visitor'),
    ('Other','Other'),
    )

    inout_choices=(
    ('In','In'),
    ('Out','Out'),
    )


    User_type=models.CharField(max_length=10,choices=user_choices)
    Name=models.CharField(max_length=20)
    In_out=models.CharField(max_length=3,choices=inout_choices)
    Date=models.DateField()
    Time=models.TimeField()

    def __str__(self):
        return '%s'%(self.Name)



class Hostel_Allocation(models.Model):
    User_type=models.ForeignKey(Hostel_Register,on_delete=models.CASCADE)
    #User_Name=models.ForeignKey(Hostel_Register,on_delete=models.CASCADE)
    Hostel_Name=models.ForeignKey(Hostel_Details,on_delete=models.CASCADE)
    Room_No=models.ForeignKey(Hostel_Room,on_delete=models.CASCADE)
    #Hostel_type=models.ForeignKey(Hostel_Details,on_delete=models.CASCADE)
    Hostel_Regd_Date=models.DateField()
    Vacating_Date=models.DateField()

    def __str__(self):
        return '%s'%(self.Room_No)

class Hostel_Visitor(models.Model):
    User_type=models.ForeignKey(Hostel_Register,on_delete=models.CASCADE)
    Visitors_Name=models.CharField(max_length=20)
    Relation=models.CharField(max_length=15)
    Date=models.DateField()
    Time=models.TimeField()

    def __str__(self):
        return '%s'%(self.Visitors_Name)
