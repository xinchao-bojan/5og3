from rest_framework import serializers
from .models import *
from custom_user.models import StudentMore, CustomUser


# class StudentMSerializer(object):
#     class Meta:
#         depth = 1
#         model = StudentM
#         fields = ['id', 'name', 'competence', 'studentm_set', 'practice_set']
#
#
# class PracticeSerializer(object):
#     class Meta:
#         depth = 1
#         model = Practice
#         fields = ['id', 'name', 'competence', 'studentm_set', 'practice_set']
#
#
# class EdCompetenceSerializer(object):
#     class Meta:
#         depth = 1
#         model = EdCompetence
#         fields = ['id', 'name', 'competence', 'studentm_set', 'practice_set']
#
#
# class InternshipSerializer(object):
#     class Meta:
#         depth = 1
#         model = Internship
#         fields = ['id', 'name', 'competence', 'studentm_set', 'practice_set']


class CustomUserOnlyNameSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = CustomUser
        fields = ['name']


class StudentMoreOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = StudentMore
        fields = ['user']


class EdOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdOrganization
        fields = ['id', 'name', 'competence', 'studentm_set', 'practice_set']

    # studentm_set = StudentMSerializer()
    # practice_set = PracticeSerializer()


class EdOrganizationOnlyNameSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdOrganization
        fields = ['id', 'name']


class EmpCompanySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmpCompany
        fields = ['id', 'name', 'internship_set', 'rate']

    # internship_set = InternshipSerializer()


class EmpCompanyOnlyNameSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmpCompany
        fields = ['id', 'name']


class EmpCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmpCompetence
        fields = ['id', 'name', 'ed_competence']

    # ed_competence = EdCompetenceSerializer()


class EdCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdCompetence
        fields = ['id', 'name', 'emp_competence']

    # emp_competence = EmpCompetenceSerializer()


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Internship
        fields = ['id', 'name', 'emp_company', 'rate', 'description', 'input_emp_competence', 'output_emp_competence']

    # emp_company = EmpCompanyOnlyNameSerializer()
    # input_emp_competence = EmpCompetenceSerializer()
    # output_emp_competence = EmpCompetenceSerializer()


class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Practice
        fields = ['id', 'name', 'ed_organization', 'description', 'input_ed_competence', 'output_ed_competence']

    # ed_organization = EdOrganizationOnlyNameSerializer()
    # input_ed_competence = EdCompetenceSerializer()
    # output_ed_competence = EdCompetenceSerializer()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Skill
        fields = ['id', 'text', 'user']

    # user = StudentMSerializer()


class StudentMSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = StudentM
        fields = ['id', 'ed_organization', 'user',
                  'ed_competence', 'emp_competence', 'rate']

    # ed_organization = EdOrganizationSerializer()
    # ed_competence = EdCompetenceSerializer()
    # emp_competence = EmpCompetenceSerializer()


class EdWorkerMSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EdWorkerM
        fields = ['id', 'ed_organization']

    # ed_organization = EdOrganizationSerializer()


class EmployerMSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmployerM
        fields = ['id', 'emp_company']

    # emp_company = EmpCompanySerializer()

class InternshipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = InternshipApplication
        fields = '__all__'