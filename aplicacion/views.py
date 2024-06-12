from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm

def inicio(request):
    return render(request, 'index.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def nuevo_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'nuevo_estudiante.html', {'form': form})