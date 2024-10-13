from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

class IsActiveEmployeePermission(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Активные сотрудники').exists()