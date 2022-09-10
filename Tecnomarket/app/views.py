from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto #cargar los modelos necesarios para traer de la db
from .forms import ContactoForm, AgregarProductoForm, CustomUserCreationForm #importar los formularios creados en el archivo forms.py
from django.contrib import messages #para los mensajes vinculados al SweetAlert2
from django.core.paginator import Paginator #clase necesaria para paginar
from django.http import Http404 #para pagina no encontrada
from django.contrib.auth import login, authenticate #para logear al usuario una vez se registre
from django.contrib.auth.decorators import login_required, permission_required #verificar los permisos para acceder a las url

# Create your views here.
#@login_required #solo permite ingresar a los usuarios authenticados
def home(request):

    productos=Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'app/home.html',data)

def contacto(request):

    data={
        "form": ContactoForm() #crear una instancia del formulario para enviarlo al template

    }

    if(request.method=='POST'): #verifico si lo q me esta enviando son datos y q el metodo sea post
        formulario=ContactoForm(data=request.POST) #creo un nuevo formulario pero con los datos q estoy enviando
        if formulario.is_valid(): #verifica q el formulario sea valido para guardarlo
            formulario.save()
            #data["mensaje"]="Gracias por Contactarnos" #crea un mensaje y lo agrega al data
            messages.success(request, "Gracias por su comentario")
            return redirect(to='home')
        else:
            data["form"]=formulario #si no es valido reenvia el mismo formulario con los errores

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request,'app/galeria.html')

@permission_required('app.add_producto') #decorador para solo permitir los que tienen permisos
def agregar_producto(request):

    data={
        "form":AgregarProductoForm
    }

    if(request.method=='POST'):
        formulario=AgregarProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente") #envia un mensaje con el texto "Agregado Correctamente"
            return redirect(to='listar_productos')
        else:
            data["form"]=formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):

    productos=Producto.objects.all()
    page = request.GET.get('page', 1) #recoger la variable page, y si no existe recoge un 1 de vuelta

    try:
        paginator=Paginator(productos, 5)
        productos=paginator.page(page)

    except:
        raise Http404

    data={
        "entity": productos,
        "paginator": paginator
    }

    return render(request, 'app/producto/listar.html', data)

@permission_required('app.change_producto')
def editar_producto(request, id):

    producto= get_object_or_404(Producto, id=id) #toma el producto de la id

    data={
        "form": AgregarProductoForm(instance=producto) #toma el formulario agregar producto con los datos del instance
    }

    if request.method=='POST':
        formulario=AgregarProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect(to='listar_productos') #te redirige al listado de productos ya editados
        else:
            data["form"]=formulario

    return render(request,'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto=get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to='listar_productos')

def registro(request):

    data = {
        "form":CustomUserCreationForm()
    }

    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"]) #rescatar los datos del formulario del usuario creado
            login(request, user) #logear el usuario con los datos rescatados en la linea anterior
            messages.success(request,"Usuario creado exitosamente")
            return redirect(to='home')
        data["form"]= formulario

    return render(request, 'registration/registro.html', data)