from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)
    nivel = models.IntegerField()
    imagen = models.ImageField(upload_to='images/')
    descripcion = models.CharField(max_length=300)

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    