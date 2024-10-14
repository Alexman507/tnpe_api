from dj_rest_auth.registration.views import RegisterView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer, CustomRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save(is_active=False)
        user.set_password(user.password)
        user.save()

    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            serializer.save(is_active=self.request.user.is_active)


class CustomRegisterView(RegisterView):
    permission_classes = [AllowAny]
    serializer_class = CustomRegisterSerializer
