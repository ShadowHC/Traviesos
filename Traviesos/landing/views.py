from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InformacionAdicionalUsuarioForm
from .models import InformacionAdicionalUsuario
from django.views.decorators.csrf import csrf_exempt
from inventario.models import Producto

def cart_view(request):
    
    return render(request, 'landing/cart.html')  

def juguetes(request):
    producto = Producto.objects.filter(Id_categoria=1)
    return render(request, 'productos/juguetes.html', {'productos': producto})

def camas_muebles(request):
    producto = Producto.objects.filter(Id_categoria=2)
    return render(request, 'productos/camas_muebles.html', {'productos': producto})

def ropas_accesorios(request):
    producto = Producto.objects.filter(Id_categoria=3)
    return render(request, 'productos/ropas_accesorios.html', {'productos': producto})

def index (request):
    return render(request, 'index.html')

@login_required
def perfil(request):
    try:
        informacion_adicional = InformacionAdicionalUsuario.objects.get(user=request.user)
    except InformacionAdicionalUsuario.DoesNotExist:
        informacion_adicional = None

    return render(request, 'login/perfil.html', {'informacion_adicional': informacion_adicional})

@login_required
def registro_informacion_adicional(request):
    if request.method == 'POST':
        formulario = InformacionAdicionalUsuarioForm(request.POST)
        if formulario.is_valid():
            informacion_adicional = formulario.save(commit=False)
            informacion_adicional.user = request.user
            informacion_adicional.save()

            messages.success(request, 'Tu información adicional se ha guardado correctamente.')

            return redirect('perfil')
    else:
        formulario = InformacionAdicionalUsuarioForm()

    return render(request, 'login/datos.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'login/registro.html', {'form': form})

@csrf_exempt 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login/login.html',{

    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('index')    