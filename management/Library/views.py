from __future__ import unicode_literals

from django.shortcuts import render
from Library.models import *
from Library.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

def libraryapp(request):
	return render(request,'libraryapp.html')

def getCategory(request):
    query =Category.objects.all()
    category_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Category_Name']= q.Category_Name
        temp_dict['Section_Code']=q.Section_Code
        category_list.append(temp_dict)
    context_dict = {'query':category_list}
    return render(request,'category.html',context_dict)

def add_catagory(request):
    if request.method == 'POST':
        Category.objects.create(
            Category_Name=request.POST['category_name'],
            Section_Code=request.POST['section_code'])
        return HttpResponseRedirect('/bookcategory')
    else:
        forms = CategoryForm()
        context_dict = {'forms':forms}
        return render (request,'categoryform.html',context_dict)

def getBook(request):
    query =Books.objects.all()
    book_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Book_Name']= q.Book_Name
        temp_dict['ISBN_No']=q.ISBN_No
        temp_dict['Purchase_date']= q.Purchase_date
        temp_dict['Book_No']=q.Book_No
        temp_dict['Auther']= q.Auther
        temp_dict['Edition']=q.Edition
        temp_dict['Category_Name']= q.Category_Name
        temp_dict['Publisher']=q.Publisher
        temp_dict['No_Of_Copies']= q.No_Of_Copies
        temp_dict['Shelf_No']=q.Shelf_No
        temp_dict['Book_Cost']= q.Book_Cost
        temp_dict['Language']=q.Language
        temp_dict['Condition']= q.Condition

        book_list.append(temp_dict)
    context_dict = {'query':book_list}
    return render(request,'book.html',context_dict)

def add_book(request):
	if request.method == 'POST':
		forms = BooksForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = BooksForm()
	context_dict = {'forms':forms}
	return render (request,'addbookform.html',context_dict)

def Issue_Book(request):
    query =Issue_Books.objects.all()
    issue_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Book_No']= q.Book_No
        temp_dict['Student_Unique_Id']=q.Student_Unique_Id
        temp_dict['Issue_date']= q.Issue_date
        temp_dict['Due_Date']=q.Due_Date
        issue_list.append(temp_dict)
    context_dict = {'query':issue_list}
    return render(request,'issue.html',context_dict)

def add_issues(request):
	if request.method == 'POST':
		forms = Issue_BooksForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = Issue_BooksForm()
	context_dict = {'forms':forms}
	return render (request,'addissuebookform.html',context_dict)

def Return_Book(request):
    query =Return_Books.objects.all()
    return_list = []
    for q in query:
        temp_dict = {}
        temp_dict['Book_No']= q.Book_No
        temp_dict['Return_or_Renewal']=q.Return_or_Renewal
        temp_dict['Date']= q.Date
        temp_dict['Fine_Amount']=q.Fine_Amount
        temp_dict['Remarks']=q.Remarks
        return_list.append(temp_dict)
    context_dict = {'query':return_list}
    return render(request,'return.html',context_dict)

def add_return(request):
	if request.method == 'POST':
		forms = Return_BooksForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = Return_BooksForm()
	context_dict = {'forms':forms}
	return render (request,'returnbookform.html',context_dict)





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class BookList(APIView):
	def get(self,request,format=None):
		library = Books.objects.all()
		serializer = BookSerializer(library,many=True)
		return Response(serializer.data)

class CategoryList(APIView):
	def get(self,request,format=None):
		library = Category.objects.all()
		serializer = CategorySerializer(library,many=True)
		return Response(serializer.data)
