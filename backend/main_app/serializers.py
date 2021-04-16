from rest_framework import serializers
from .models import *


class EdOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdOrganization

class EmpCompanySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmpCompany

class EmpCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmpCompetence

class EdCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdCompetence

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Internship

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Practice

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Skills


