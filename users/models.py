from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


#BaseManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    realname = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email,password,**extra_fields): #createsuperuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario necesita que is_staff sea verdadero")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario necesita que is_superuser sea verdadero")

        return self.create_user(email=email, password=password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    email=models.CharField(max_length=80,unique=True)
    username = models.CharField(max_length=45)
    date_or_birth=models.DateField(null=True)

    objecs= CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.email
