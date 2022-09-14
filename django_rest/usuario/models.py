from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return self.nombre