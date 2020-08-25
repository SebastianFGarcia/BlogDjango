from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django import forms

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Nombres', max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellidos',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(RegistroUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class UpdateUsuarioForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Nombres', max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellidos',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(label='Último inicio de sesión',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(label='Es superusuario', max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(label = 'Es staff',max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(label = 'Activo', max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(label='Fecha de alta',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','last_login','is_superuser','is_staff','is_active','date_joined')

class CambioContraseñaForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña antigua:', max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(label='Contraseña nueva:',max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(label='Contraseña nueva (confirmación):',max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')