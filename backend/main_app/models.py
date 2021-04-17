from django.contrib.auth import get_user_model
from django.db import models

from custom_user.models import StudentMore, EdWorkerMore, EmployerMore


class Internship(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    emp_company = models.ForeignKey('EmpCompany', verbose_name='Работодатель', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание стажировки')

    input_emp_competence = models.ManyToManyField('EmpCompetence', related_name='input_emp_competence')
    output_emp_competence = models.ManyToManyField('EmpCompetence', related_name='output_emp_competence')

    def __str__(self):
        return self.name


class InternshipApplication(models.Model):
    ed_organization = models.ForeignKey('EdOrganization', on_delete=models.CASCADE, null=True)
    internship = models.ForeignKey('Internship', on_delete=models.CASCADE)
    student = models.ForeignKey('StudentM', on_delete=models.CASCADE)


class Practice(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование стажировки')
    ed_organization = models.ForeignKey('EdOrganization', verbose_name='Образовательная организация',
                                        on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание практики')
    input_ed_competence = models.ManyToManyField('EdCompetence', related_name='input_ed_competence')
    output_ed_competence = models.ManyToManyField('EdCompetence', related_name='output_ed_competence')

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название навыка')

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
    emp_competence = models.ManyToManyField('EmpCompetence', blank=True)

    def __str__(self):
        return self.name


'''
SubUser
'''


class StudentM(models.Model):
    user = models.OneToOneField(StudentMore, on_delete=models.CASCADE)
    ed_organization = models.ForeignKey(EdOrganization, on_delete=models.CASCADE)
    ed_competence = models.ManyToManyField(EdCompetence)
    emp_competence = models.ManyToManyField('EmpCompetence')

    def __str__(self):
        return self.ed_organization


class EmployerM(models.Model):
    user = models.OneToOneField(EmployerMore, on_delete=models.CASCADE)
    emp_company = models.ForeignKey('EmpCompany', on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class EdWorkerM(models.Model):
    user = models.OneToOneField(EdWorkerMore, on_delete=models.CASCADE)
    ed_organization = models.ForeignKey('EmpCompany', on_delete=models.CASCADE)

    def __str__(self):
        return self.user


'''
EMP
'''


class EmpCompetence(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компетенции', unique=True)

    def __str__(self):
        return self.name


class EmpCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название организации-работодателя')

    def __str__(self):
        return self.name


'''
REVIEW
'''


class ReviewOnStudent(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название отзыва')
    review_text = models.TextField(verbose_name='Отзыв')
    rate = models.PositiveSmallIntegerField(verbose_name='Оценка', default=0)
    employer = models.ForeignKey('EmployerM', verbose_name='Работодатель', on_delete=models.CASCADE)
    student_for_review = models.ForeignKey('StudentM', verbose_name='Отзыв на студента', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.rate > 5:
            self.rate = 5
        return super().save(*args, **kwargs)


class ReviewOnEmployer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Заголовок отзыва')
    review_text = models.TextField(verbose_name='Отзыв')
    rate = models.PositiveSmallIntegerField(default=0, verbose_name='Оценка')
    student = models.ForeignKey('StudentM', verbose_name='Студент', on_delete=models.CASCADE)
    employer_for_review = models.ForeignKey('EmpCompany', verbose_name='Отзыв о работодателе', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.rate > 5:
            self.rate = 5
        return super().save(*args, **kwargs)
