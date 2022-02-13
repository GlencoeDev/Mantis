import zoneinfo
import pytz
from timezone_field import TimeZoneField
from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if email is None:
            raise TypeError("Users must have an email address")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(first_name, last_name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    dislay_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    timezone = TimeZoneField(
        use_pytz=True, default="Asia/Dubai", choices_display="WITH_GMT_OFFSET"
    )
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name="date joined", editable=False, auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name="last login", editable=False, auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name="last login", editable=False, auto_now=True
    )

    # User Image Upload Functionality to be implemented
    # avatar = models.ImageField(upload_to='avatars/',blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
