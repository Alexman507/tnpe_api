from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        read_only_fields = ['is_active']

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['is_active'] = False
        return data