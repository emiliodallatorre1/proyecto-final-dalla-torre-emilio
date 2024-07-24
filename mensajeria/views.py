from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mensaje
from .forms import MensajeForm

@login_required
def chat(request):
    mensajes = Mensaje.objects.all().order_by('-fecha_envio')[:50]
    form = MensajeForm()
    return render(request, 'mensajeria/chat.html', {'mensajes': mensajes, 'form': form})

@login_required
@csrf_exempt
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

@login_required
def obtener_mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-fecha_envio')[:50]
    data = [{'emisor': m.emisor.username, 'contenido': m.contenido, 'fecha': m.fecha_envio.strftime('%d/%m/%Y %H:%M')} for m in mensajes]
    return JsonResponse(data, safe=False)