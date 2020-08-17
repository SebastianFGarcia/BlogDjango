from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
	titulo = models.CharField(max_length = 255)
	titulo_tag = models.CharField(max_length = 255, default="Blog")
	autor = models.ForeignKey(User, on_delete = models.CASCADE)
	cuerpo = models.TextField()
	fecha_publicacion = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.titulo + ' | ' + str(self.autor)

	def get_absolute_url(self):
		return reverse('detalle-publicacion', args=(str(self.id)))
