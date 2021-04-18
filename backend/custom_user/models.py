from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Customer must have all necessary information')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email=self.normalize_email(email), password=password, **kwargs)
        user.type = CustomUser.Type.ADMIN
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    class Type(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        ADMIN = 'ADMIN', 'Admin'
        EMPLOYER = 'EMPLOYER', 'Employer'
        EDWORKER = 'EDWORKER', 'Edworker'

    type = models.CharField(_('Type'), max_length=15, choices=Type.choices, blank=True)

    email = models.EmailField(verbose_name='Адрес электронной почты', max_length=63, unique=True)
    first_name = models.CharField(max_length=127, verbose_name='Имя')
    last_name = models.CharField(max_length=127, verbose_name='Фамилия')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.type:
            self.is_active = True
        super().save(*args, **kwargs)
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def make_active(self):
        self.is_active = True

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


class StudentMore(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    FEMALE = 0
    MALE = 1
    SEX_CHOICER = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    sex = models.IntegerField(choices=SEX_CHOICER)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Type.STUDENT)


class Student(CustomUser):
    objects = StudentManager()

    @property
    def more(self):
        return self.studentmore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Type.STUDENT
        return super().save(*args, **kwargs)


class AdminMore(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Type.ADMIN)


class Admin(CustomUser):
    objects = AdminManager()

    @property
    def more(self):
        return self.adminmore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Type.ADMIN
        return super().save(*args, **kwargs)


class EmployerMore(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class EmployerManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Type.EMPLOYER)


class Employer(CustomUser):
    objects = EmployerManager()

    @property
    def more(self):
        return self.employermore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Type.EMPLOYER
        return super().save(*args, **kwargs)


class EdWorkerMore(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class EdWorkerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Type.EDWORKER)


class EdWorker(CustomUser):
    objects = EdWorkerManager()

    @property
    def more(self):
        return self.edworkermore

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = CustomUser.Type.EDWORKER
        return super().save(*args, **kwargs)
