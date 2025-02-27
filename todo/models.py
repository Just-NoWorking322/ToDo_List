from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^\+996\d{9}$",
        message="Номер телефона должен быть в формате +996 XXX XXX XXX (9 цифр после +996)"
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[phone_regex],
        blank=True,  # Разрешаем пустое поле, чтобы избежать ошибок в `createsuperuser`
        null=True,    # Позволяет хранить `NULL` в БД
        db_index=True # Ускоряет поиск по полю
    )
    age = models.PositiveIntegerField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
