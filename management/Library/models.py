from __future__ import unicode_literals
from django.db import models
from Student.models import Student_Admission

class Category(models.Model):
    Category_Name=models.CharField(max_length=15)
    Section_Code=models.DecimalField(max_digits=10,decimal_places=0)

    def __str__(self):
        return '%s'%(self.Category_Name)


class Books(models.Model):
    Condition_choices=(
    ('As-New','As-New'),
    ('Fine','Fine'),
    ('Good','Good'),
    ('Fair','Fair'),
    ('Poor','Poor'),
    ('Missing','Missing'),
    ('Lost','Lost'),
    )

    Book_Name=models.CharField(max_length=25)
    ISBN_No=models.DecimalField(max_digits=13,decimal_places=0)
    Purchase_date=models.DateField()
    Book_No=models.CharField(max_length=5)
    Auther=models.CharField(max_length=15)
    Edition=models.CharField(max_length=10)
    Category_Name=models.ForeignKey(Category,on_delete=models.CASCADE)
    Publisher=models.CharField(max_length=20)
    No_Of_Copies=models.DecimalField(max_digits=3,decimal_places=0)
    Shelf_No=models.DecimalField(max_digits=5,decimal_places=0)
    Book_Cost=models.DecimalField(max_digits=10,decimal_places=2)
    Language=models.CharField(max_length=15)
    Condition=models.CharField(max_length=8,choices=Condition_choices)

    def __str__(self):
        return '%s'%(self.Book_Name)


class Issue_Books(models.Model):
    Book_No=models.ForeignKey(Books,on_delete=models.CASCADE)
    Student_Unique_Id=models.ForeignKey(Student_Admission,on_delete=models.CASCADE)
    Issue_date=models.DateField()
    Due_Date=models.DateField()

    def __str__(self):
        return '%s'%(self.Book_No)


class Return_Books(models.Model):
    rr_choice=(
    ('Return','Return'),
    ('Renewal','Renewal'),
    )

    Book_No=models.ForeignKey(Books,on_delete=models.CASCADE)
    Return_or_Renewal=models.CharField(max_length=7,choices=rr_choice)
    Date=models.DateField()
    Fine_Amount=models.DecimalField(max_digits=10,decimal_places=2)
    Remarks=models.TextField()

    def __str__(self):
        return '%s'%(self.Book_No)
