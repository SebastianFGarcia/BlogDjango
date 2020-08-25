from django.urls import path
from .views import RegistroUsuarioView, ActualizarUsuarioView, CambioContraseñaView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('registration/', RegistroUsuarioView.as_view(), name = 'registro'),
    path('edit_user/', ActualizarUsuarioView.as_view(), name = 'editar_usuario'),
    path('password/', CambioContraseñaView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password_success'),
]

