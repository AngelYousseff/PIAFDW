from django.db import models

class Encuesta(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha = models.DateField()
    telefono = models.CharField(max_length=15)
    genero = models.CharField(max_length=10)
    educacion = models.CharField(max_length=100)
    correo = models.EmailField()
    password = models.CharField(max_length=100)
    comentarios = models.TextField()
    terminos = models.BooleanField()

    def _str_(self):
        return self.nombre