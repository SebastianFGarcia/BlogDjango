from django.urls import path
from .views import HomeView, DetallePublicacion

urlpatterns = [
	path('', HomeView.as_view(), name = "home"),
	path('post/<int:pk>', DetallePublicacion.as_view(), name = 'detalle-publicacion')
]
