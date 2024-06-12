from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    # v1
    # return HttpResponse('Bienvenidos a mi INICIO!!')
    return render(request, 'aplicacion/index.html')
