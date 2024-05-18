from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone_no = models.IntegerField()
    alternative_phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True)
    alternative_address = models.CharField(max_length=250, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone_no', 'address', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email