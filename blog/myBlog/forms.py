from django import forms
from .models import Post, Categoria


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'categorias', 'autor', 'header_image', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el titulo'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'categorias': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba el Cuerpo de la publicación'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el titulo'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba el Cuerpo de la publicación'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('__all__')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba la categoria'}),
        }
