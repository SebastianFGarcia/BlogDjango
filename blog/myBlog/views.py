from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post, Categoria
from .forms import PostForm, EditForm, CategoriaForm

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = 	['-fecha_publicacion']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categorias'] = Categoria.objects.all()
		return context

class DetallePublicacion(DetailView):
	model = Post
	template_name = 'Post/show.html'
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		stuff = get_object_or_404(Post, id= self.kwargs['pk'])
		total_likes = stuff.total_likes()
		context['categorias'] = Categoria.objects.all()
		context['total_likes'] = total_likes
		return context
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

def CategoriaView(request, pk):
	categorias_post = Post.objects.filter(categorias_id = pk)
	categoria = categorias_post.first()
	return render(request, 'Post/listcategoria.html', { 'categoria' : categoria, 'categorias_post' : categorias_post })

def LikeView(request, pk):
	post = get_object_or_404(Post, id = request.POST.get('post_id'))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('detalle-publicacion', args=[str(pk)]))