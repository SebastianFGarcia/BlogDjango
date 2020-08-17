from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Categoria
from .forms import PostForm, EditForm, CategoriaForm

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = 	['-fecha_publicacion']


class DetallePublicacion(DetailView):
	model = Post
	template_name = 'Post/show.html'

class CrearPublicacion(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'Post/create.html'

class ActualizarPublicacion(UpdateView):
	model = Post
	template_name = 'Post/update.html'
	form_class = EditForm 

class EliminarPublicacion(DeleteView):
	model = Post
	template_name = 'Post/delete.html'
	success_url = reverse_lazy('home')

class ListCategoriaView(ListView):
	model = Categoria
	template_name = 'Categoria/index.html'
	ordering = 	['-id']
class CrearCategoriaView(CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'Categoria/create.html'

class ActualizarCategoriaView(UpdateView):
	model = Categoria
	template_name = 'Categoria/update.html'
	form_class = CategoriaForm

class EliminarCategoriaView(DeleteView):
	model = Categoria
	template_name = 'Categoria/delete.html'
	success_url = reverse_lazy('listar_categoria')