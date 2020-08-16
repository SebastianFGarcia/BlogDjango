from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
	model = Post
	template_name = 'home.html'


class DetallePublicacion(DetailView):
	model = Post
	template_name = 'detalle_publicacion.html'

class CrearPublicacion(CreateView):
	model = Post
	template_name = 'create.html'
	fields = '__all__'