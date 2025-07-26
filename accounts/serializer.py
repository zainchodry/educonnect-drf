from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default='student')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user
