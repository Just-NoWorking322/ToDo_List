from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from tasks.models import Todo  # Импортируем Todo из tasks

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'age', 'is_staff')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    actions = ['activate_users']

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
    activate_users.short_description = "Активировать выбранных пользователей"