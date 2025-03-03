from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
import re

class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()  # Используем PhoneNumberField для валидации номера телефона

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'age', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # extra_kwargs должен быть внутри Meta

    def validate_phone_number(self, value):
        # Дополнительная валидация для номера телефона (формат +996)
        if not re.match(r'^\+996\d{9}$', str(value)):
            raise serializers.ValidationError("Номер телефона должен быть в формате +996XXXXXXXXX")
        return value

    def create(self, validated_data):
        # Создание пользователя с хешированием пароля
        user = User.objects.create_user(**validated_data)
        return user