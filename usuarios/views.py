from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import UserRegisterForm, UserEditForm, PasswordChangeForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Inicia sesión ahora.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'¡Bienvenido/a {user.username}!')
            return redirect('perfil')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '¡Sesión cerrada!')
    return redirect('login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado!')
            return redirect('editar_perfil')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Contraseña cambiada!')
            return redirect('cambiar_pass')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/change_password.html', {'form': form})
