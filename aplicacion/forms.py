from django import forms
from .models import Estudiante, Materia
from django.forms.widgets import DateInput

class EstudianteForm(forms.ModelForm):
    materias = forms.MultipleChoiceField(
        choices=Materia.OPCIONES_MATERIAS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    fecha_nacimiento = forms.DateField(
        widget=DateInput(format='%d/%m/%Y'),  
        input_formats=['%d/%m/%Y'] 
    )
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'avatar', 'fecha_nacimiento', 'materias']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            materias = self.cleaned_data.get('materias')
            if materias:
                instance.materias.clear()
                for materia_nombre in materias:
                    materia, _ = Materia.objects.get_or_create(nombre=materia_nombre)
                    instance.materias.add(materia)
        
        return instance
class BuscarEstudiante(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)