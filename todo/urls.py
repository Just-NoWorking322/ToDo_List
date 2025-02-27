from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TodoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"todos", TodoViewSet, basename="todo")  # Добавляем таски

urlpatterns = [
    path("", include(router.urls)),  
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
