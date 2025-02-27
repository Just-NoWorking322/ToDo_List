from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^\+996\d{9}$",
        message="Номер телефона который вы вводите должен быть в формате +996 XXX XXX (6 цифр после +996)"
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[phone_regex],
        blank=False
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username