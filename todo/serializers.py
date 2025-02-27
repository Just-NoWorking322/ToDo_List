from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "phone_number", "age", "created_at", "password"]
        extra_kwargs = {
            "email": {"required": True, "allow_blank": False},
            "username": {"required": True, "allow_blank": False},
            "phone_number": {"required": True, "allow_blank": False},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
'''
password = serializers.CharField(write_only=True, min_length=8) — скрываем пароль при выводе и делаем минимальную длину 8 символов.
extra_kwargs — указываем, что email, username и phone_number обязательны.
create() — используем create_user, чтобы пароль хешировался автоматически.
'''