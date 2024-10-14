from dj_rest_auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UserViewSet, CustomRegisterView

app_name = UsersConfig.name
router = SimpleRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path("user/register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
]
