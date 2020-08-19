from django.urls import path
from .views import *

urlpatterns = [
	path('', HomeView.as_view(), name = "home"),
	path('post/<int:pk>', DetallePublicacion.as_view(), name = 'detalle-publicacion'),
	path('create/', CrearPublicacion.as_view(), name = 'crear_publicacion'),
	path('post/edit/<int:pk>',ActualizarPublicacion.as_view(), name= 'actualizar-publicacion'),
	path('post/<int:pk>/delete', EliminarPublicacion.as_view(), name= 'eliminar-publicacion'),
	path('categoria/', ListCategoriaView.as_view(), name = 'listar_categoria'),
	path('categoria/create/', CrearCategoriaView.as_view(), name = 'crear_categoria'),
	path('categoria/edit/<int:pk>',ActualizarCategoriaView.as_view(), name= 'actualizar-categoria'),
	path('categoria/<int:pk>/delete', EliminarCategoriaView.as_view(), name= 'eliminar-categoria'),
	path('categoria/<int:pk>/', CategoriaView, name='categorias')
]
