from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.Model):
    role = models.CharField(max_length=50, default="client")

    def __str__(self):
        return self.role


class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        UserRole, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return self.username
