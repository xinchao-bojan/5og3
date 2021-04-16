from django.db import models


# Create your models here.

class Internship(models.Model):
    name = models.CharField(max_length=127, verbose_name='Наименование стажировки')
    emp_company = models.ForeignKey('EmpCompany', verbose_name='Работодатель', on_delete=models.CASCADE)


class EdOrganization(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название образовательной организации')
    address = models.CharField(max_length=127, verbose_name='Адрес образовательной организации')


class EdCompetence(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название компетенции')
    # EmpCompetence = models.ManyToManyField()


class EmpCompetence(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название компетенции')


class EmpCompany(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название организации-работодателя')
    address = models.CharField(max_length=127, verbose_name='Адрес организации-работодателя')
