from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Student
        exclude = ['password']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CustomUser
        exclude = ['password']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Admin
        exclude = ['password']


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employer
        exclude = ['password']


class EdWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdWorker
        exclude = ['password']
