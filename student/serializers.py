from rest_framework import serializers
from student.models import Student
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'last_name', 'date_of_birth', 'phone', 'gender']