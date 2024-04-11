from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=150)