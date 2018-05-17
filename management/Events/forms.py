from django import forms
from Events.models import *

class typeForm(forms.ModelForm):
	class Meta:
		model = Event_Type
		fields = '__all__'

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = '__all__'
