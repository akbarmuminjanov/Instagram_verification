from django.db import models

# Create your models here.

class Accaunt(models.Model):
    username = models.CharField(max_length=150, verbose_name="user")
    password = models.CharField(max_length=150, verbose_name="password")


    def __str__(self):
        return str(f"{self.username}")