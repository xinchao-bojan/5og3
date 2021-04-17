from django.contrib.auth import get_user_model
from django.db import models

from custom_user.models import StudentMore, EdWorkerMore


class Internship(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    emp_company = models.ForeignKey('EmpCompany', verbose_name='Работодатель', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание стажировки')
    input_emp_competence = models.ManyToManyField('EmpCompetence', related_name='input_emp_competence')
    output_emp_competence = models.ManyToManyField('EmpCompetence', related_name='output_emp_competence')

    def __str__(self):
        return self.name


class Practice(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    ed_organization = models.ForeignKey('EdOrganization', verbose_name='Образовательная организация',
                                        on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание практики')
    input_ed_competence = models.ManyToManyField('EdCompetence', related_name='input_ed_competence')
    output_ed_competence = models.ManyToManyField('EdCompetence', related_name='output_ed_competence')

    def __str__(self):
        return self.name


'''
ED
'''


class EdOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название образовательной организации')
    competence = models.ManyToManyField('EdCompetence')

    def __str__(self):
        return self.name


class EdCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции', unique=True)
    emp_competence = models.ManyToManyField('EmpCompetence', related_name='emp_to_ed_competence', blank=True)

    def __str__(self):
        return self.name


'''
SubUser
'''


class StudentM(models.Model):
    user = models.OneToOneField(StudentMore, on_delete=models.CASCADE)
    ed_organization = models.ForeignKey(EdOrganization, on_delete=models.CASCADE)


class Worker(models.Model):
    user = models.OneToOneField(EdWorkerMore, on_delete=models.CASCADE)
    ed_organization = models.ForeignKey(EdOrganization, on_delete=models.CASCADE)


'''
EMP
'''


class EmpCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции')
    ed_competence = models.ManyToManyField('EdCompetence', related_name='ed_to_emp_competence', blank=True)

    def __str__(self):
        return self.name


class EmpCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название организации-работодателя')

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название навыка')

    def __str__(self):
        return self.name
