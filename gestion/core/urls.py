from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('fv/',myfirstview, name='first'),
    path('dashboard/', home, name='home'),
    path('category/listar/', CategoryListView.as_view(), name='listarCat'),
    path('category/crear/', CategoryCreateView.as_view(), name='crearCat'),
    path('category/editar/<int:pk>/', CategoryUpdateView.as_view(), name='editarCat'),
    path('category/eliminar/<int:pk>/', CategoryDeleteView.as_view(), name='eliminarCat'),
    #path('category/form/', CategoryFormView.as_view(), name='formCat'),
    #path('category/listar/', CategoryListView, name='listarCat'),
    #path('productos/listar/', ProductoListView.as_view(), name='listProd'),
    path('product/listar/', ProductListView.as_view(), name='listarPro'),
    path('product/crear/', ProductCreateView.as_view(), name='crearPro'),
    path('product/editar/<int:pk>/', ProductUpdateView.as_view(), name='editarPro'),
    path('product/eliminar/<int:pk>/', ProductDeleteView.as_view(), name='eliminarPro'),
]