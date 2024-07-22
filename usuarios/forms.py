from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm as DjangoPasswordChangeForm
from .models import Usuario

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']

class PasswordChangeForm(DjangoPasswordChangeForm):
    class Meta:
        model = Usuario
        fields = ['old_password', 'new_password1', 'new_password2']
