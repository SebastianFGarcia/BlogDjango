from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm, UpdateUsuarioForm, CambioContraseñaForm

class RegistroUsuarioView(generic.CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class ActualizarUsuarioView(generic.UpdateView):
    form_class = UpdateUsuarioForm
    template_name = 'registration/edit.html'
    success_url = reverse_lazy('home')
        
    def get_object(self):
        return self.request.user
class CambioContraseñaView(PasswordChangeView):
    form_class = CambioContraseñaForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration\password_success.html',{})
