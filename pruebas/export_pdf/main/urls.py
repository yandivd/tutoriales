from django.urls import path
from .views import *

urlpatterns = [
    path('', ImprimirPDF.as_view(), name='imprimir'),
    path('1/',index),
]