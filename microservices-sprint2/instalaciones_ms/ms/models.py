from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    caracteristicas = models.TextField()

    def __str__(self):
        return self.nombre

