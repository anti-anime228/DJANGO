from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=15, unique=True,verbose_name='username')
    email = models.EmailField(unique=True,verbose_name='email')
    first_name = models.CharField(max_length=15, verbose_name='first_name')
    last_name = models.CharField(max_length=15, verbose_name='last_name')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username



class Secret(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Секрет {self.id}: {self.text}"
