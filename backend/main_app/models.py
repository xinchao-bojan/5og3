from django.db import models

# Create your models here.

class Internship(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    emp_company = models.ForeignKey('EmpCompany', verbose_name='Работодатель', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание стажировки')
    input_emp_competence = models.ManyToManyField('EmpCompetence')
    output_emp_competence = models.ManyToManyField('EmpCompetence')


class Practice(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    ed_organization = models.ForeignKey('EdOrganization', verbose_name='Образовательная организация', on_delete=CASCADE)
    description = models.TextField(verbose_name='Описание практики')
    input_ed_competence = models.ManyToManyField('EdCompetence')
    output_ed_competence = models.ManyToManyField('EdCompetence')


class EdOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название образовательной организации')

class EdCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции')
    emp_competence = models.ManyToManyField('EmpCompetence')

class EmpCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции')
    ed_competence = models.ManyToManyField('EdCompetence')

class EmpCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название организации-работодателя')
    
    
