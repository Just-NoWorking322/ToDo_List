from django.urls import path
from .views import TodoListView, TodoDetailView, TodoDeleteAllView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('delete-all/', TodoDeleteAllView.as_view(), name='todo-delete-all'),
]