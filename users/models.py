from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils.crypto import get_random_string

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=250, blank=True)
    account_no = models.CharField(max_length=100, unique=True)
    user_pin = models.PositiveIntegerField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone_no', 'address', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.account_no:
            self.account_no = self.generate_account_no()
        super().save(*args, **kwargs)

    def generate_account_no(self):
        prefix = 'ACC'
        unique_no = get_random_string(length=10, allowed_chars='0123456789')
        return f'{prefix}{unique_no}'