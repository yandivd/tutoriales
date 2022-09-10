from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo=models.CharField(max_length=50)
    fecha_fab=models.DateField()
    imagen=models.ImageField(upload_to='Productos', null=True, blank=True)

    def __str__(self):
        return self.nombre

#creacion de las choices para el tipo de consulta
opciones_consultas=[
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"]
]

class Contacto(models.Model):
    nombre= models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()
    aviso=models.BooleanField()

    def __str__(self):
        return self.nombre
