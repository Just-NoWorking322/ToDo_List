from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer, TodoCreateSerializer

# Список всех задач и создание новой задачи
class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только задачи текущего пользователя
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Автоматически привязываем задачу к текущему пользователю
        serializer.save(user=self.request.user)

# Детализация, обновление и удаление задачи
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только задачи текущего пользователя
        return Todo.objects.filter(user=self.request.user)

# Удаление всех задач пользователя
class TodoDeleteAllView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только задачи текущего пользователя
        return Todo.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        # Удаляем все задачи пользователя
        self.get_queryset().delete()
        return Response(status=204)