from .models import *
from rest_framework import serializers

class HostelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_Details
        fields = '__all__'

class HostelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_Room
        fields = '__all__'

class HostelRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_Register
        fields = '__all__'
