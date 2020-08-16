from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','titulo_tag','autor','cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Escriba el titulo'}),
            'titulo_tag': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Escriba el Cuerpo de la publicación'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','titulo_tag','cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Escriba el titulo'}),
            'titulo_tag': forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Escriba el Cuerpo de la publicación'}),
        }