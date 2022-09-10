import random

from django.http import Http404, JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.core.paginator import Paginator
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.

def home(request):
    return render(request, 'core/home.html',{'title': 'Dashboard'})

class CategoryListView(ListView):
    model = Category
    template_name = 'core/category/list.html'

    #para devolver el queryset filtrado
 #   def get_queryset(self):
 #        return Category.objects.filter(nombre__startswith='D')
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,** kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'searchdata':
                data=[]
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error']="Ha ocurrido un error"
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

 #modificando el diccionario que se le envia al template

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Categorias"
        #context['object_list'] = Producto.objects.all()
        context['create_url']=reverse_lazy('crearCat')
        context['list_url']=reverse_lazy('listarCat')
        return context

 #create view para crear registros de un model determinado

class CategoryCreateView(CreateView):
    model=Category
    form_class=CategoryForm
    template_name='core/category/create.html'
    success_url=reverse_lazy('listarCat')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action=='add':
                form=CategoryForm(request.POST)
                #linea para llamar al save del formulario
                #data=form.save()
                #######Para hacer el AJAX desde el Post
                if form.is_valid():
                    form.save()
                else:
                    data['error']=form.errors
            else:
                data['error']="No entro ninguna opcion"
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

        self.object=None
        context=self.get_context_data(**kwargs)
        context['form']=form
        return render(request, self.template_name,context)

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Categoria"
        context['action']='add'
        context['list_url']=reverse_lazy('listarCat')
        
        #context['object_list'] = Producto.objects.all()
        return context 

class CategoryUpdateView(UpdateView):
    model=Category
    form_class=CategoryForm
    template_name='core/category/create.html'
    success_url=reverse_lazy('listarCat')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action=='edit':
                form=self.get_form()
                data=form.save()
            else:
                data['error']="No ha ingresado ninguna opcion"
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Editar Categoria'
        context['list_url']=reverse_lazy('listarCat')
        context['action']='edit'
        return context

class CategoryDeleteView(DeleteView):
    model=Category
    template_name='core/category/delete.html'
    success_url=reverse_lazy('listarCat')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            self.object.delete()
        except Exception as e:
            data['error']=str(e)
        return HttpResponseRedirect(redirect_to='/core/category/listar/')
        #return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Categoria"
        context['list_url']=reverse_lazy('listarCat')
        return context


class CategoryFormView(FormView):
    form_class = CategoryForm
    template_name ='core/category/create.html'
    success_url = reverse_lazy('listarCat')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'form | Categoria'
        context['list_url']= reverse_lazy('listarCat')
        context['action']='add'
        return context


class ProductListView(ListView):
    model=Producto
    template_name='core/productos/list.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']="Listado de Productos"
        return context

class ProductCreateView(CreateView):
    model=Producto
    form_class=ProductForm
    template_name='core/productos/create.html'
    success_url=reverse_lazy('listarPro')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    '''def post(self, request, *args, **kwargs):
        data={}
        try:
            print(request.POST)
            print(request.FILES)

        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)'''

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Producto"
        context['action']='add'
        context['list_url']=reverse_lazy('listarPro')
        
        #context['object_list'] = Producto.objects.all()
        return context

class ProductUpdateView(UpdateView):
    model=Producto
    form_class=ProductForm
    template_name='core/productos/create.html'
    success_url=reverse_lazy('listarPro')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Editar Producto'
        context['list_url']=reverse_lazy('listarPro')
        context['action']='edit'
        return context

class ProductDeleteView(DeleteView):
    model=Producto
    template_name='core/productos/delete.html'
    success_url=reverse_lazy('listarPro')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Producto"
        context['list_url']=reverse_lazy('listarPro')
        return context