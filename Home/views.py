from django.shortcuts import render, HttpResponse 

def inicio(request):
	return render(request,"Home/index.html")

def usuario(request):
	return render(request,"Home/iniciosesion.html")#Registro de usuario

def newinicio(request):
	return render(request,"Home/ultimo.html")# Confirmación de registro de usuario y detalles del mismo Botón a "inicio"

def regPro(request):
	return render(request,"Inicio/RegPro.html")#crea un producto o servicio.Botón para ver el detalle.

def detPro(request):
	return render(request,"Inicio/DetPro.html")# 2 botones: para volver a inicio o para modificar.

def modPro(request):
	return render(request,"Inicio/ModPro.html")# botón aceptar que vaya a detalle.

def regCom(request):
	return render(request,"Inicio/RegCom.html")#crea un comercio u oficio.Botón para ver el detalle.

def detCom(request):
	return render(request,"Inicio/DetCom.html")# 2 botones: para volver a inicio o para modificar.

def modCom(request):
	return render(request,"Inicio/ModCom.html")# botón aceptar que vaya a detalle.

