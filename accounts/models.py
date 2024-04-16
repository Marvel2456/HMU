from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if email is None:
            raise TypeError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        if password is None:
            raise TypeError('Password is required')

        user = self.create_user(email, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        } 
