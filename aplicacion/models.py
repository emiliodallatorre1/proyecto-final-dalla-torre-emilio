from django.db import models
from django.conf import settings
import datetime

class Materia(models.Model):
    OPCIONES_MATERIAS = [
        ('matematica', 'Matemática'),
        ('lengua', 'Lengua'),
        ('naturales', 'Ciencias Naturales'),
    ]
    nombre = models.CharField(max_length=50, choices=OPCIONES_MATERIAS, unique=True)

    def __str__(self):
        return self.get_nombre_display()

class Estudiante(models.Model):
    profesor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='estudiantes')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    materias = models.ManyToManyField(Materia, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.fecha_nacimiento:
            self.fecha_nacimiento = datetime.date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"