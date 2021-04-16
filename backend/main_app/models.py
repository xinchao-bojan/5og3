from django.db import models

# Create your models here.
Стажировка
кмопетенции
образовательная органиазция
Работа
class Internship(models.Model):
    name = models.CharField(max_length=127, verbose_name='Наименование стажировки')
    emp_company = models.ForeignKey('EmpCompany', verbose_name='Работодатель', on_delete=models.CASCADE)



class EdOrganization(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название организации')

class Competence(model.Model):

class EmpCompany(models.Model):