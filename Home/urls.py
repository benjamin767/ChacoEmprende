from django.urls import path
from Home import views

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('usuario/', views.usuario, name = 'Usuario'),
    path('newinicio/', views.newinicio, name = 'Newinicio'),
    path('regPro/', views.regPro, name = 'RegPro'),
    path('detPro/', views.detPro, name = 'DetPro'),
    path('modPro/', views.modPro, name = 'ModPro'),
    path('regCom/', views.regCom, name = 'RegCom'),
    path('detCom/', views.detCom, name = 'DetCom'),
    path('modCom/', views.modCom, name = 'ModCom'),

]