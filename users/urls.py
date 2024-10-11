from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig.name
router = SimpleRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
]
