from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

class HomeView(ListView):
	model = Post
	template_name = 'home.html'


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