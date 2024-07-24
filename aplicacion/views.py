from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Materia
from .forms import EstudianteForm, BuscarEstudiante
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

def inicio(request):
    return render(request, 'aplicacion/index.html')

@login_required
def lista_estudiantes(request):
    formulario = BuscarEstudiante(request.GET)
    
    if request.user.is_superuser:
        estudiantes = Estudiante.objects.all()
    else:
        estudiantes = Estudiante.objects.filter(profesor=request.user)
        
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        apellido = formulario.cleaned_data.get('apellido')
        
        if nombre:
            estudiantes = estudiantes.filter(nombre__icontains=nombre)
        if apellido:
            estudiantes = estudiantes.filter(apellido__icontains=apellido)

    return render(request, 'aplicacion/lista_estudiantes.html', {'estudiantes': estudiantes, 'formulario': formulario})

@login_required
def nuevo_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            estudiante = form.save(commit=False)
            estudiante.profesor = request.user
            estudiante.save()
            materias_seleccionadas = form.cleaned_data.get('materias', [])
            for materia_nombre in materias_seleccionadas:
                materia, _ = Materia.objects.get_or_create(nombre=materia_nombre)
                estudiante.materias.add(materia)

            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'aplicacion/nuevo_estudiante.html', {'form': form})

@login_required
def ver_estudiante(request, estudiante_id):
    if request.user.is_superuser:
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    else:
        estudiante = get_object_or_404(Estudiante, id=estudiante_id, profesor=request.user)
    return render(request, 'aplicacion/ver_estudiante.html', {'estudiante': estudiante})

@login_required
def editar_estudiante(request, estudiante_id):
    if request.user.is_superuser:
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    else:
        estudiante = get_object_or_404(Estudiante, id=estudiante_id, profesor=request.user)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('ver_estudiante', estudiante_id=estudiante.id)
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'aplicacion/editar_estudiante.html', {'form': form, 'estudiante': estudiante})

@login_required
def eliminar_estudiante(request, estudiante_id):
    if request.user.is_superuser:
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    else:
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'aplicacion/eliminar_estudiante.html', {'estudiante': estudiante})

