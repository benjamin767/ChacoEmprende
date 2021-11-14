from django.urls import path
from Formulario import views
from Formulario.models import Negocio, Producto


urlpatterns = [
	
	path("login/", views.login, name ='Logueate'),
	path("nuevo_registro/", views.nuevo_registro, name = 'Registro'),
	path("exito/", views.exito, name ='Exito'),
]