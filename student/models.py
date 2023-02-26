from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone = models.IntegerField()
    class Gender(models.TextChoices):
        FEMALE = 'FEM', 'Female'
        MALE = 'MALE', 'Male'
        OTHER = 'OTHER', 'Other'
    gender = models.CharField(max_length=5, choices=Gender.choices)
    user = models.OneToOneField(User, on_delete=models.CASCADE)