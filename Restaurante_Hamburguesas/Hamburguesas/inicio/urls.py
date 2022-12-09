from django.urls import path
from .views import index, acercade, base, secion, empleados, agregarEmpreado, sucursal, agregarSucursal, registro, eliminarS, editarS, guardarS, eliminarE, editarE, guardarE, inicioSecion, cerrar_sesion, TablaHambur, agregarHamburguesa, eliminarH, editarH, guardarH, producto

# Para nuestras direcciones.
urlpatterns = [
    path('', index, name = "inicio"),
    path('inicioSecion/', inicioSecion, name = "inicioSecion"),
    #------------------------------------------------------------
    path('producto/', producto, name="producto"),
    #------------------------------------------------------------
    path('cerrar_sesion/', cerrar_sesion, name = "cerrar_sesion"),
    path('about/', acercade, name = "about"),
    path('secion/', secion, name = "secion"),
    path('base/', base, name="base"),
    path('registro/',registro, name="registro"),
    #------------------------------------------------------------
    path('sucursal/', sucursal, name="sucursal"),
    path('agregarSucursal/', agregarSucursal),
    path('eliminarS/<id>', eliminarS, name="eliminarS"),
    path('editarS/<id>', editarS, name="editarS"),
    path('guardarS/<id>', guardarS, name="guardarS"),
    #-------------------------------------------------------------
    path('empleados/', empleados, name="empleados"),
    path('agregarEmpreado/', agregarEmpreado),
    path('eliminarE/<id>', eliminarE, name="eliminarE"),
    path('editarE/<id>', editarE, name="editarE"),
    path('guardarE/<id>', guardarE, name="guardarE"),
    #-------------------------------------------------------------
    path('TablaHambur/', TablaHambur, name="TablaHambur"),
    path('agregarHamburguesa/', agregarHamburguesa , name="agregarHamburguesa"),
    path('eliminarH/<id>', eliminarH, name="eliminarH"),
    path('editarH/<id>', editarH, name="editarH"),
    path('guardarH/<id>', guardarH, name="guardarH"),

]

 



