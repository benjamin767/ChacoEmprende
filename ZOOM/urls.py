from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('Formulario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]