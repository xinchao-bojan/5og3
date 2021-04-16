from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Customer must have all necessary information')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    class Type(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        ADMIN = 'ADMIN', 'Admin'
        EMPLOYER = 'EMPLOYER', 'Employer'
        EDWORKER = 'EDWORKER', 'Edworker'

    type =models.CharField(_('Type'))

    email = models.EmailField(verbose_name='Адрес электронной почты', max_length=63, unique=True)
    first_name = models.CharField(max_length=127, verbose_name='Имя')
    last_name = models.CharField(max_length=127, verbose_name='Фамилия')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name', ]
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def make_active(self):
        self.is_active = True

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    #
    # def has_module_perms(self, app_label):
    #     return True

    class Student(models.Model):

    class Admin(models.Model):

    class Employer(models.Model):

    class EdWorker(models.Model):
