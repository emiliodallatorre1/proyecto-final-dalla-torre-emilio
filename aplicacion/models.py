# aplicacion/models.py

from django.db import models

class Estudiante(models.Model):
    nombre= models.CharField(max_length=20)
    edad= models.IntegerField()
    correo= models.EmailField()

    def __str__(self):
        return self.nombre
