from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description')
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        queryset.update(is_completed=True)
    mark_as_completed.short_description = "Отметить выбранные задачи как выполненные"