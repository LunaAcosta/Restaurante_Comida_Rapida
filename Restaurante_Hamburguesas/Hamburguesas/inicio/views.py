from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Empleado, Sucursal, Hamburguesas, TipoCarne
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def acercade(request):
    return render(request,'acerca.html')

def base(request):
    return render(request, 'base.html')

def producto(request):
    hamburguesas = Hamburguesas.objects.all()
    return render(request, 'producto.html',{"hamburguesas":hamburguesas})


def secion(request):
    return render(request, 'secion.html')

def inicioSecion(request):
    if request.method == "POST":
        username = request.POST.get("InputUsername")
        password = request.POST.get("InputPassword")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            return redirect("inicioSecion")
    return render(request, 'InicioSecion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect("inicioSecion")

def registro(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'registro.html', {"form":form})

#----------------------------------------------------------------------------------------------------------------------------------
# CRUD para sucursal
def sucursal(request):
    sucursal = Sucursal.objects.all()
    return render(request, 'sucursal.html', {"sucursal":sucursal})

def agregarSucursal(request):
    nombre = request.POST['inputNombreSucursal']
    direccion = request.POST['inputDireccion']
    telefono = request.POST['inputTelefono']

    sucursal = Sucursal.objects.create(
        nombre = nombre,
        direccion =direccion,
        telefono = telefono,
    )
    return redirect('/sucursal')

def editarS(request, id): 
    sucursal = Sucursal.objects.get(id=id)
    return render(request,'editarS.html', {"sucursal": sucursal})

def guardarS(request, id):
    nombre = request.POST['inputNombreSucursal']
    direccion = request.POST['inputDireccion']
    telefono = request.POST['inputTelefono']

    sucursal = Sucursal.objects.get(id=id)
    sucursal.nombre = nombre
    sucursal.direccion = direccion
    sucursal.telefono = telefono
    sucursal.save()
    return redirect('/sucursal')

def eliminarS(request, id):
    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    return redirect('/sucursal')
#----------------------------------------------------------------------------------------------------------------------------------

# CRUD para empleado
def empleados(request):
    empleado = Empleado.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'empleados.html', {"empleado":empleado,"sucursales" : sucursales })

def agregarEmpreado(request):
    if request.method == 'POST':
        emp = Empleado.objects.create(
        nombre =   request.POST.get('inputNombre'),
        apellio =  request.POST.get('inputApellido'),
        puesto =   request.POST.get('inputCargo'),
        sucursal = Sucursal.objects.get(id=request.POST.get('inputSucursales')),
        horario = request.POST.get('inputHorario')
        )
        emp.save()
    return redirect('/empleados')

def editarE(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request,'editarE.html', {"empleado": empleado})

def guardarE(request, id):
    emp = Empleado.objects.get(id=id)  
    if request.method == "POST":
        emp.nombre =   request.POST.get('inputNombre')
        emp.apellio =  request.POST.get('inputApellido')
        emp.puesto =   request.POST.get('inputCargo')
        emp.sucursal = Sucursal.objects.get(id=request.POST.get('inputSucursales'))
        emp.horario = request.POST.get('inputHorario')
        emp.save()
        return redirect('empleados')

def eliminarE(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('/empleados')


# CRUD Hamburguesa ---------------------------------------------------------------------------------------------------

def TablaHambur(request):
    tablaHambur = Hamburguesas.objects.all()
    agTipoCarne = TipoCarne.objects.all()
    agSucursal = Sucursal.objects.all()
    return render(request, 'hamburguesa.html', {"tablaHambur":tablaHambur, "agTipoCarne": agTipoCarne, "agSucursal": agSucursal })

def agregarHamburguesa(request):
    if request.method == 'POST':
        agregar = Hamburguesas.objects.create(
        nombre = request.POST.get('inputHambur'),
        tipoCarme = TipoCarne.objects.get(id=request.POST.get('inputTipo')),
        tamaño = request.POST.get('inputTamaño'),
        numeroCarne = request.POST.get('inputNCarne'),
        vegetales = request.POST.get('inputVegetales'),
        precio = request.POST.get('inputPrecio'),
        sucursal = Sucursal.objects.get(id=request.POST.get('inputSucursales'))
        )
        agregar.save()
    return redirect('producto')

def editarH(request, id):
    hamburguesa = Hamburguesas.objects.get(id=id)
    tiposCarnes = TipoCarne.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request,'editarH.html', {"hamburguesa": hamburguesa, "tiposCarnes": tiposCarnes, "sucursales": sucursales})

def guardarH(request, id):
    guardar = Hamburguesas.objects.get(id=id)  
    if request.method == "POST":
        guardar.nombre = request.POST.get('inputHambur')
        guardar.tipoCarme = TipoCarne.objects.get(id=request.POST.get('inputTipo'))
        guardar.tamaño = request.POST.get('inputTamaño')
        guardar.numeroCarne = request.POST.get('inputNCarne')
        guardar.vegetales = request.POST.get('inputVegetales')
        guardar.precio = request.POST.get('inputPrecio')
        guardar.sucursal = Sucursal.objects.get(id=request.POST.get('inputSucursales'))
        guardar.save()
        return redirect('producto')

def eliminarH(request, id):
    eliminarH = Hamburguesas.objects.get(id=id)
    eliminarH.delete()
    return redirect('/producto')







    

