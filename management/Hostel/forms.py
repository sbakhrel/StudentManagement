from django import forms
from Hostel.models import *



class Hostel_DetailsForm(forms.ModelForm):
	class Meta:
		model = Hostel_Details
		fields = '__all__'

class Hostel_RoomForm(forms.ModelForm):
	class Meta:
		model = Hostel_Room
		fields = '__all__'

class Hostel_RegisterForm(forms.ModelForm):
	class Meta:
		model = Hostel_Register
		fields = '__all__'

class Hostel_AllocationForm(forms.ModelForm):
	class Meta:
		model = Hostel_Allocation
		fields = '__all__'
