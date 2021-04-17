from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Student
        exclude = ['password', 'email']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CustomUser
        exclude = ['password', 'email']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Admin
        exclude = ['password', 'email']


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employer
        exclude = ['password', 'email']


class EdWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdWorker
        exclude = ['password', 'email']
