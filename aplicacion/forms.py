from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'edad', 'correo']

class BuscarEstudiante(forms.Form):
    estudiante=forms.CharField(max_length=20, required=False)