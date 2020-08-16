from django.urls import path
from .views import HomeView, DetallePublicacion, CrearPublicacion

urlpatterns = [
	path('', HomeView.as_view(), name = "home"),
	path('post/<int:pk>', DetallePublicacion.as_view(), name = 'detalle-publicacion'),
	path('create/', CrearPublicacion.as_view(), name = 'crear_publicacion')
]
