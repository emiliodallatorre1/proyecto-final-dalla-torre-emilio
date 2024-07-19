from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm, BuscarEstudiante

def inicio(request):
    return render(request, 'aplicacion/index.html')

def lista_estudiantes(request):
    # estudiantes = Estudiante.objects.all()
    formulario=BuscarEstudiante(request.GET)
    if formulario.is_valid():
        nombre=formulario.cleaned_data['estudiante']
        estudiantes=Estudiante.objects.filter(nombre=nombre)
    return render(request, 'aplicacion/lista_estudiantes.html', {'estudiantes': estudiantes})
    

def nuevo_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'aplicacion/nuevo_estudiante.html', {'form': form})

# def buscar_estudiante(request):
#     formulario=BuscarEstudiante(request.GET)
#     if formulario.is_valid():
#         nombre=formulario.cleaned_data('nombre')
#         estudiante=Estudiante.objects.filter(nombre=nombre)
#     return render(request, 'aplicacion/lista_estudiantes.html', {'estudiante': estudiante, 'formulario':formulario})