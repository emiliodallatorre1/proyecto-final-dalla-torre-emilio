from django.urls import path
from .views import register, login, logout, edit_profile, change_password

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registro/', register, name='registro'),
    path('perfil/', edit_profile, name='perfil'),
    path('perfil/editar/', edit_profile, name='editar_perfil'),
    path('perfil/contrasena/', change_password, name='cambiar_pass'),
]
