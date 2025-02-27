from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TodoViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"todos", TodoViewSet, basename="todo")  # Добавляем таски

urlpatterns = [
    path("", include(router.urls)),  
]
