from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega1.models import * #importo todas las clases de models 
#from AppEntrega1.forms import ....... ESTO CUANDO HAGA LOS FORMS!

#creo las vistas, una por cada html. salvo la del padre.html q no va.

def inicio(request):   
    return render(request, 'AppEntrega1/inicio.html')

def bodega(request):   
    return render(request, 'AppEntrega1/bodega.html')

def vino(request):   
    return render(request, 'AppEntrega1/vino.html')

def cliente(request):   
    return render(request, 'AppEntrega1/cliente.html')

#ahora faltan las de los forms.


# dejo estas vistas viejas como comentario por si las necesito. 
'''def bodega(self):
    bodega=Bodega(nombre='Santa Julia', email= santajulia@santajulia.com)
    bodega.save()
    texto=f'bodega {bodega.nombre}, email {bodega.email}'
    return HttpResponse(texto)

def vino(self):
    vino=Vino(nombre='GranPinot', varietal= 'pinot', bodega='Trapiche')
    vino.save()
    texto=f'Vino {vino.nombre}, varietal {vino.varietal}, de bodega {vino.bodega}'
    return HttpResponse(texto)

def cliente(self):
    cliente=Cliente(nombre='Gerardo Morales', email=gm@gm.com, pais='Ecuador')
    cliente.save()
    texto=f'cliente {cliente.nombre}, email: {cliente.email}, pais: {cliente.pais}'
    return HttpResponse(texto)'''