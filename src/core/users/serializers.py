from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'last_login', 'date_joined', 'groups', 'user_permissions')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'last_login', 'date_joined', 'groups', 'user_permissions')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_activity')
        read_only_fields = ('id', 'last_login', 'date_joined', 'groups', 'user_permissions')
