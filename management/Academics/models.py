from __future__ import unicode_literals
from django.db import models
from Student.models import *

class Course(models.Model):

    Course_name=models.CharField(max_length=15)
    Description=models.TextField()
    Code=models.CharField(max_length=10)
    Minimum_attendance_in_percent=models.DecimalField(max_digits=2, decimal_places=0)
    Total_Working_Days=models.DecimalField(max_digits=2,decimal_places=0)

    def __str__(self):
        return '%s'%(self.Course_name)

class Batch(models.Model):
    Course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch_name=models.CharField(max_length=20)
    Start_date=models.DateField()
    End_Date=models.DateField()
    Max_no_of_student=models.DecimalField(max_digits=2,decimal_places=0)
    def __str__(self):
        return '%s'%(self.Batch_name)

class Subject(models.Model):
    Subject_name=models.CharField(max_length=20)
    Subject_code=models.CharField(max_length=10)
    Subject_description=models.TextField()

    def __str__(self):
        return '%s'%(self.Subject_name)

class Exam(models.Model):
    term_choice=(
    ('First_Term','First_Term'),
    ('Second_term','Second_term'),
    ('Third_Term','Third_Term'),
    ('Final_Term','Final_Term')
    )
    Term=models.CharField(max_length=10,choices=term_choice)
    Exam_Name=models.CharField(max_length=15)
    Subject_code=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Student_Unique_Id=models.ForeignKey(Student_Admission,on_delete=models.CASCADE)
    Full_marks=models.DecimalField(max_digits=3,decimal_places=0)
    Pass_marks=models.DecimalField(max_digits=3,decimal_places=0)
    Marks_obtained=models.DecimalField(max_digits=3,decimal_places=0)

    def __str__(self):
        return '%s'%(self.Exam_Name)


class Assignment(models.Model):
    Assignment_Title=models.CharField(max_length=30)
    Assignment_Description=models.TextField()
    #Attachments=File Attachments
    Course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch_name=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Subject_code=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Date_Of_Submission=models.DateField()

    def __str__(self):
        return '%s'%(self.Assignment_Title)

class Notes(models.Model):
    Notes_Title=models.CharField(max_length=30)
    Notes_Description=models.TextField()
    #Attachments=File Attachments
    Course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch_name=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Subject_code=models.ForeignKey(Subject,on_delete=models.CASCADE)


    def __str__(self):
        return '%s'%(self.Notes_Title)


class Certificates(models.Model):
    Certificate_type=models.CharField(max_length=20)
    def __str__(self):
        return '%s'%(self.Certificate_type)

class Alumni(models.Model):
    pass
