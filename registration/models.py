from django.db import models
from django.contrib.auth.models import User


class RegisterUser(models.Model):
    class Meta:
        verbose_name = "Register User"
        verbose_name_plural = "Register User"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
