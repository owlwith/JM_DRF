from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=15, unique=True)
    Password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
