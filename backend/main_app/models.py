from django.db import models


# Create your models here.

class Internship(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    emp_company = models.ForeignKey('EmpCompany', verbose_name='Работодатель', on_delete=models.CASCADE)


class EdOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название образовательной организации')


class EdCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции')
    emp_competence = models.ManyToManyField('EmpCompetence')


class EmpCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции')
    ed_competence = models.ManyToManyField(EdCompetence)


class EmpCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название организации-работодателя')
