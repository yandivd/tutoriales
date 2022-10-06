from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
# Register your models here.
admin.site.register(Category, CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
