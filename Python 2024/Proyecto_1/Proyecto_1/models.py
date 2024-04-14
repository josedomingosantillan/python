from django.db import models

class dbo_alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_pa = models.CharField(max_length=50)
    apellido_ma = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=30)
    carrera = models.CharField(max_length=20)
    sexo = models.CharField(max_length=200)
