from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Importando los modelos
from .models import Rescatado, Usuario

# Cosas para la autentificación
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required

# Cargar contenido dentro de los modal
from django.views.generic import UpdateView, ListView

# Cargando REST
from .serializers import UsuarioSerializer, RescatadoSerializer
from rest_framework import viewsets

# Templates
def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'Index.html',{'usuario':usuario})

def contactanos(request):
    usuario = request.session.get('usuario',None)
    return render(request,'Contactanos.html',{'usuario':usuario})

def galeria(request):
    usuario = request.session.get('usuario',None)

    if request.POST.get('seleccion'):
        filtro = request.POST.get('seleccion',False)
        rescatados = Rescatado.objects.filter(estado=filtro)
    else:
        rescatados = Rescatado.objects.all()

    return render(request,'Galeria.html',{'rescatados':rescatados, 'usuario':usuario})

def registro(request):
    usuario = request.session.get('usuario',None)
    return render(request,'Registro.html',{'usuario':usuario})

# Crear un nuevo usuario desde el Registro
def crear(request):
    rut = request.POST.get('rut',False)
    username = request.POST.get('nombre',False)
    fechanacimiento = request.POST.get('fechanacimiento',False)
    telefono = request.POST.get('telefono',False)
    email = request.POST.get('email',False)
    region = request.POST.get('region',False)
    comuna = request.POST.get('comuna',False)
    vivienda = request.POST.get('vivienda',False)
    cpassword = request.POST.get('cpassword',False)
    usuario = Usuario(rut=rut, username=username, fechanacimiento=fechanacimiento, telefono=telefono,
    email=email, region=region, comuna=comuna, vivienda=vivienda, password=cpassword)
    usuario.set_password(cpassword)
    usuario.save()
    return redirect("registro")

# Agregar un nuevo Rescate
@login_required(login_url='login')
def nuevoRescate(request):
    nombre = request.POST.get('nombre',False)
    descripcion = request.POST.get('descripcion',False)
    raza = request.POST.get('raza',False)
    foto = request.FILES['foto']
    rescatado = Rescatado(nombre=nombre, descripcion=descripcion, raza=raza, estado='Rescatado', foto=foto)
    rescatado.save()
    return redirect(galeria)

# Editar un Rescate
@login_required(login_url='login')
def editarRescate(request):
    nombre = request.POST.get('editNombre',False)
    descripcion = request.POST.get('editDescripcion',False)
    raza = request.POST.get('editRaza',False)
    estado = request.POST.get('editEstado',False)
    foto = request.FILES['editFoto']
    id = request.POST.get('editId',0)
    rescatado = Rescatado.objects.get(pk = id)
    rescatado.nombre = nombre
    rescatado.descripcion = descripcion
    rescatado.raza = raza
    rescatado.estado = estado
    rescatado.foto = foto
    rescatado.save()
    return redirect('galeria')

# Adoptar
def adoptarRescate(request,id):
    rescatado = Rescatado.objects.get(pk = id)
    rescatado.estado = 'Adoptado'
    rescatado.save()
    return redirect('galeria')

# Borrar un Rescate
@login_required(login_url='login')
def borrarRescate(request,id):
    rescatado = Rescatado.objects.get(pk = id)
    rescatado.delete()
    return redirect('galeria')

# Autentificación template
def login(request):
    return render(request,'Login.html',{})

# La acción de iniciar sesión
def loginIniciar(request):
    email = request.POST.get('email',False)
    contrasenia = request.POST.get('contrasenia',False)
    usuario = authenticate(request, username=email, password=contrasenia)
    if usuario is not None:
        request.session['usuario'] = usuario.email
        auth_login(request, usuario)
        return redirect('index')
    else:
        return redirect("login")

# Cerrando sesión
@login_required(login_url='login')
def cerrarSession(request):
    del request.session['usuario']
    logout(request)
    return redirect('index')

# API
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RescatadoViewSet(viewsets.ModelViewSet):
    queryset = Rescatado.objects.all()
    serializer_class = RescatadoSerializer