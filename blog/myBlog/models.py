from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
	titulo = models.CharField(max_length = 255)
	titulo_tag = models.CharField(max_length = 255, default="Blog")
	autor = models.ForeignKey(User, on_delete = models.CASCADE)
	cuerpo = models.TextField()

	def __str__(self):
		return self.titulo + ' | ' + str(self.autor)
