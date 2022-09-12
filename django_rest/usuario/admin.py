from django.contrib import admin
from .models import *

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Usuario, UsuarioAdmin)