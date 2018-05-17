from django import forms
from Student.models import *



class GradeForm(forms.ModelForm):
	class Meta:
		model = Student_Grade
		fields = '__all__'

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student_Admission
		fields = '__all__'

class FacultyForm(forms.ModelForm):
	class Meta:
		model = Student_Faculty
		fields = '__all__'
