from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        superuser = self.model(email=email, **extra_fields)
        superuser.role = "admin"
        superuser.set_password(password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save()
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICE = (
        ('reception', 'Reception'),
        ('admin', 'Admin'),
        ('technician', 'Technician'),
        ('inspector', 'Inspector'),
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    role = models.CharField(max_length=255, choices=ROLE_CHOICE)
    objects = UserManager()

    def __str__(self):
        return self.email


class Car(models.Model):
    car_name = models.CharField(max_length=255)
    is_repair = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    part = models.ManyToManyField('CarPart')

    def __str__(self):
        return self.car_name


class CarPart(models.Model):
    part_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.part_name
