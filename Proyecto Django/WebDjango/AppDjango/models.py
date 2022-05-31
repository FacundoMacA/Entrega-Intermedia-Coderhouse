from django.db import models

# Create your models here.
class Torneos(models.Model):
    nombre = models.CharField(max_length=50)
    año = models.IntegerField()
    pais = models.CharField(max_length=50)
    duracion = models.IntegerField()
    campeon = models.CharField(max_length=100)

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()
    estadio = models.CharField(max_length=100)
    provincia = models.CharField(max_length=50)

class Jugadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    equipo = models.CharField(max_length=100)
    posicion = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)