from django import forms
from Library.models import *

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'

class BooksForm(forms.ModelForm):
	class Meta:
		model = Books
		fields = '__all__'

class Issue_BooksForm(forms.ModelForm):
	class Meta:
		model = Issue_Books
		fields = '__all__'

class Return_BooksForm(forms.ModelForm):
	class Meta:
		model = Return_Books
		fields = '__all__'
