from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="電話番号")
    address = models.TextField(blank=True, null=True, verbose_name="住所")