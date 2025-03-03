from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Указываем уникальные related_name для полей groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set',  # Уникальное имя для обратной ссылки
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Уникальное имя для обратной ссылки
        related_query_name='user',
    )

    def __str__(self):
        return self.username