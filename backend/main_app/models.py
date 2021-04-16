from django.db import models

# Create your models here.
# цифро
class Internship(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    emp_company = models.ForeignKey('EmpCompany', verbose_name='Работодатель', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание стажировки')
    input_emp_competence = models.ManyToManyField('EmpCompetence', related_name='input_emp_competence')
    output_emp_competence = models.ManyToManyField('EmpCompetence', related_name='output_emp_competence')


class Practice(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    ed_organization = models.ForeignKey('EdOrganization', verbose_name='Образовательная организация',
                                        on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание практики')
    input_ed_competence = models.ManyToManyField('EdCompetence', related_name='input_ed_competence')
    output_ed_competence = models.ManyToManyField('EdCompetence', related_name='output_ed_competence')


class EdOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название образовательной организации')

class EdCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции')
    emp_competence = models.ManyToManyField('EmpCompetence', related_name='emp_to_ed_competence')

class EmpCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции')
    ed_competence = models.ManyToManyField('EdCompetence', related_name='ed_to_emp_competence')

class EmpCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название организации-работодателя')


class Skills(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название навыка')