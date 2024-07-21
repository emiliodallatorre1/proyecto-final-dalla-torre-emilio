from django.urls import path
from .views import register, login, logout, edit_profile, change_password

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', edit_profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/password/', change_password, name='change_password'),
]
