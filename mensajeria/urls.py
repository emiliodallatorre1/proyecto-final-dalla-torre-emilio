from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('obtener/', views.obtener_mensajes, name='obtener_mensajes'),
]