import logging

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        read_only_fields = ["is_active"]


class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "is_active"]

