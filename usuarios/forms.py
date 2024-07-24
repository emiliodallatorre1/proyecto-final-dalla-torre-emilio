from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm as DjangoPasswordChangeForm
from .models import Usuario

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Nombre de Usuario', max_length=20)
    name=forms.CharField(label='Nombre', max_length=20)
    last_name=forms.CharField(label='Apellido', max_length=20)
    email = forms.EmailField(label='Correo Electrónico')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)
    biografia = forms.CharField(label='Biografía', max_length=250)    
    class Meta:
        model = Usuario
        fields = ['username','name','last_name','email', 'avatar', 'biografia', 'password1', 'password2']


class UserEditForm(UserChangeForm):
    password=None
    username=forms.CharField(label='Nombre de Usuario', max_length=20, required=False)
    email = forms.EmailField(label='Correo Electrónico', required=False)
    avatar = forms.ImageField(label='Avatar', required=False)
    biografia = forms.CharField(label='Biografía', required=False)    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'avatar','biografia']

class PasswordChangeForm(DjangoPasswordChangeForm):
    old_password = forms.CharField(
            label="Contraseña actual",
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    new_password1 = forms.CharField(
            label="Nueva contraseña",
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    new_password2 = forms.CharField(
            label="Confirmar nueva contraseña",
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']

class InicioSesionForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))