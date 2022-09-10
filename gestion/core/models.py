from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from django.conf import settings

# Create your models here.

class Type(models.Model):
    nombre= models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['id']


class Category(models.Model):
    nombre= models.CharField(max_length=100, verbose_name='Nombre', unique=True)

    descripcion=models.TextField( max_length=500, verbose_name='Descripcion', null=True, blank=True)


    def __str__(self):
        return self.nombre

    def toJSON(self):
        item=model_to_dict(self)
        return item
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['id']

class Employer(models.Model):
    category=models.ManyToManyField(Category)
    type= models.ForeignKey(Type, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=200, verbose_name='Nombres')
    dni= models.CharField(max_length=11, verbose_name='DNI', unique=True)
    fecha_registro= models.DateField(default=datetime.now , verbose_name='Fecha de Registro')
    fecha_creado=models.DateTimeField(auto_now=True)
    fecha_actualizacion=models.DateTimeField(auto_now_add=True)
    edad=models.PositiveIntegerField(default=0)
    salario=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado=models.BooleanField(default=True)
    genero=models.CharField(max_length=1, default='M')
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    curriculum=models.FileField(upload_to='cv/%Y/%m/%d')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table = 'Empleados'
        ordering = ['id']

class Producto(models.Model):
    nombre=models.CharField(max_length=55)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Productos', blank=True, null=True)
    pvp=models.DecimalField(default=0.0, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nombre

    def get_image(self):
        if self.image:
            return '{}{}'.format(settings.MEDIA_URL, self.image)
        else:
            return '{}{}'.format(settings.STATIC_URL,'img/empty.png' )


