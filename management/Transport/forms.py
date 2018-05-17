from django import forms
from Transport.models import *



class VehicleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = '__all__'

class RouteForm(forms.ModelForm):
	class Meta:
		model = Route
		fields = '__all__'

class DriverForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields = '__all__'

class Transport_AllocationForm(forms.ModelForm):
	class Meta:
		model = Transport_Allocation
		fields = '__all__'
