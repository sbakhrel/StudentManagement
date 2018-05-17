from __future__ import unicode_literals
from django.db import models
from Student.models import *

class Student_Grade(models.Model):
    Grade=models.CharField(max_length=15)

    def __str__(self):
        return '%s'%(self.Grade)


class Student_Faculty(models.Model):
    Faculty=models.CharField(max_length=15)

    def __str__(self):
        return '%s'%(self.Faculty)
class Student_Admission(models.Model):
    #choice list for gender
    gender_choices = (
		('Male','Male'),
		('Female','Female'),
		('Other','Other'),
		('Prefer not to specify','Prefer not to specify')
		)
    #choice list for blood group
    blood_choices = (
		('A+','A+'),
		('A-','A-'),
		('AB+','AB+'),
		('AB-','AB-'),
        ('B+','B+'),
		('B-','B-'),
		('O+','O+'),
		('O','O-'),
		)
    # choice list for Religion
    religion_choices = (
		('Hinduism','Hinduism'),
		('Buddhism','Buddhism'),
		('Islam','Islam'),
		('Cristianity','Cristianity'),
        ('Other','Other'),
		)

    # choice list for state
    state_choices = (
		('State-1','State-1'),
		('State-2','State-2'),
		('Stat-3','State-3'),
		('State-4','State-4'),
        ('State-5','State-5'),
        ('State-6','State-6'),
        ('State-7','State-7'),
		)

    hostel_choices=(
        ('Day','Day'),
        ('Full','Full'),
        ('No','No'),
    )

    Transportation_choices=(
        ('Yes','Yes'),
        ('No','No')
    )


    #personal Information
    First_Name=models.CharField(max_length=10)
    Middle_Name=models.CharField(max_length=10)
    Family_Name=models.CharField(max_length=10)
    Student_Unique_Id=models.AutoField(primary_key=True)
    Date_of_birth=models.DateField()
    Gender=models.CharField(max_length=25,choices=gender_choices)
    Blood_Group=models.CharField(max_length=5,choices=blood_choices)
    Birth_place=models.CharField(max_length=20)
    Nationality=models.CharField(max_length=10)
    Mother_Tangue=models.CharField(max_length=10)
    Faculty=models.ForeignKey(Student_Faculty,on_delete=models.CASCADE)
    Grade=models.ForeignKey(Student_Grade,on_delete=models.CASCADE)
    Religion=models.CharField(max_length=10,choices=religion_choices)
    National_Identity_card_type=models.CharField(max_length=15)
    National_ID_Card_Number=models.CharField(max_length=10)
    #photo = models.ImageField(upload_to='image/%Y/%m/%d', default='there_is_no_image.jpg')

    #Contact details
    Permanent_Address=models.CharField(max_length=25)
    Present_Address=models.CharField(max_length=25)
    City=models.CharField(max_length=25)
    Zip=models.CharField(max_length=5)
    State=models.CharField(max_length=10,choices=state_choices)
    Country=models.CharField(max_length=25)
    Phone=models.DecimalField(max_digits=10, decimal_places=0)
    Mobile=models.DecimalField(max_digits=10, decimal_places=0)
    Email=models.EmailField()

    #Parent details
    Fathers_Name=models.CharField(max_length=25)
    Fathers_Contact_Number=models.DecimalField(max_digits=10, decimal_places=0)
    fathers_Profession=models.CharField(max_length=15)
    Fathers_National_ID_Card_Number=models.CharField(max_length=10)

    Mothers_Name=models.CharField(max_length=25)
    Mothers_Contact_Number=models.DecimalField(max_digits=10, decimal_places=0)
    Mothers_Profession=models.CharField(max_length=15)
    Mothers_National_ID_Card_Number=models.CharField(max_length=10)

    Local_Parents_Name=models.CharField(max_length=25)
    Relationship=models.CharField(max_length=15)
    Local_Parents_Profession=models.CharField(max_length=15)
    Income=models.DecimalField(max_digits=10, decimal_places=2)

    #previous qualification details
    Previous_School_Name=models.CharField(max_length=25)
    Previous_School_Address=models.CharField(max_length=25)
    Latest_Qualification=models.CharField(max_length=10)

    #others
    Hostel=models.CharField(max_length=10,choices=hostel_choices)
    Transportation=models.CharField(max_length=10,choices=Transportation_choices)



    def __str__(self):
        return '%s%s'%(self.First_Name,self.Family_Name)
