from django.urls import path
from AppEntrega1.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('vino/', vino, name= 'vino'),
    path('bodega/', bodega, name= 'bodega'),
    path('cliente/', cliente, name= 'cliente'),
]