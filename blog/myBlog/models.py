from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date

class Categoria(models.Model):
	nombre = models.CharField(max_length = 255)
	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('listar_categoria')
		
class Post(models.Model):
	titulo = models.CharField(max_length = 255)
	titulo_tag = models.CharField(max_length = 255, default="Blog")
	categorias = models.ForeignKey(Categoria, on_delete= models.CASCADE)
	autor = models.ForeignKey(User, on_delete = models.CASCADE)
	cuerpo = models.TextField()
	fecha_publicacion = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='blog_post')

	def __str__(self):
		return self.titulo + ' | ' + str(self.autor)

	def get_absolute_url(self):
		return reverse('detalle-publicacion', args=(str(self.id)))
	
	def total_likes(self):
		return self.likes.count()
