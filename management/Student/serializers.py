from .models import *
from rest_framework import serializers

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Grade
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Faculty
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Admission
        fields = '__all__'
