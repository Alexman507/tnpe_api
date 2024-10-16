from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import default, slugify

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = models.CharField(max_length=150, **NULLABLE, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, verbose_name="email")
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", **NULLABLE
    )
    is_active = models.BooleanField(default=False, verbose_name="Активен")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
