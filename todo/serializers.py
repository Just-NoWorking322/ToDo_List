from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^\+996\d{9}$",
                message="Номер телефона должен начинаться с +996 и содержать 9 цифр после кода страны.",
            )
        ]
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "phone_number", "age", "created_at", "password"]
        extra_kwargs = {
            "email": {"required": True, "allow_blank": False},
            "username": {"required": True, "allow_blank": False},
            "phone_number": {"required": True, "allow_blank": False},
        }

    def create(self, validated_data):
        """Создаём пользователя с хешированным паролем."""
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """Обновляем пользователя, хешируем пароль, если передан."""
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # Шифруем пароль
        instance.save()
        return instance

    
'''
password = serializers.CharField(write_only=True, min_length=8) — скрываем пароль ри выводе и делаем минимальную длину 8 симвлов
extra_kwargs  указываем, что email, username и phone_number обязательны
create()  используем create_user, чтобы пароль хешировался автоматически
''' 


'''
password стал необязательным при обновлении
update() теперь хеширует пароль если он передан

'''