from django.urls import path
from .views import RegistroUsuarioView

urlpatterns = [
    path('registration/', RegistroUsuarioView.as_view(), name = 'registro'),
]

