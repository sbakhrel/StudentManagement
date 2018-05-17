from .models import *
from rest_framework import serializers

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Type
        fields = '__all__'
