from django import forms
from Academics.models import *

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = '__all__'

class BatchForm(forms.ModelForm):
	class Meta:
		model = Batch
		fields = '__all__'

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'

class ExamForm(forms.ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = '__all__'

class NotesForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = '__all__'

class CertificatesForm(forms.ModelForm):
	class Meta:
		model = Certificates
		fields = '__all__'

class AlumniForm(forms.ModelForm):
	class Meta:
		model = Alumni
		fields = '__all__'
