from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import UserRegisterForm, UserEditForm, PasswordChangeForm, InicioSesionForm

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Inicia sesión ahora.')
            return redirect('login')
   
    return render(request, 'usuarios/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'¡Bienvenido/a {user.username}!')
            next_url = request.GET.get('next')
            return redirect(next_url or 'inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = InicioSesionForm()
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '¡Sesión cerrada!')
    return redirect('inicio')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user )
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado!')
            return redirect('inicio')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Contraseña cambiada correctamente!')
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/cambiar_pass.html', {'form': form})
