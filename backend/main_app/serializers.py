from rest_framework import serializers
from .models import *


class EdOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdOrganization
        fields = '__all__'


class EmpCompanySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmpCompany
        fields = '__all__'


class EmpCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmpCompetence
        fields = '__all__'


class EdCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdCompetence
        fields = '__all__'


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Internship
        fields = '__all__'


class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Practice
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Skill
        fields = '__all__'


class StudentMSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = StudentM
        fields = '__all__'


class EdWorkerMSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = StudentM
        fields = '__all__'


class EmployerMSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmployerM
        fields = '__all__'


class InternshipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = InternshipApplication
        fields = '__all__'
