from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import * #VER SI LOS NECESITO AL AVANZAR EN ESTAS VISTAS
from accounts.forms import *  #IDEM
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

#vista home de accounts: hace falta?
def inicio(request):   
    return render(request, 'accounts/inicio.html')

def usuario(request):
    return render(request, 'accounts/usuario.html')

#login. 
def login_request(request):
    #aagregar q si ya estoy logueado no entre??, muestre cartel"ya estas logueado", y me mande a donde estaba.(igual el boton ya esto ok login/logout)
    if request.method=='POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= request.POST['username'] 
            clave= request.POST['password'] #notar es sin enie!
            user=authenticate(username=usuario, password=clave)
            if user is not None: #ie si hace match con alguno
                login(request, user) #usa el login de django...?, xq el nuestro es login_request...
                return render(request, 'accounts/inicio.html', {'form':form, 'mensaje':f'bienvenido  {usuario}'})
            else:
                return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'usuario o clave incorrecta'})    
        else:
            return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'FORMULARIO INVALIDO'} )
    else:  #si es GET
        form=AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form}) #lo mando al login con el form vacio

#registro
def register(request):
    #agregar q si ya estoy logueado no entre??
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, 'accounts/inicio.html', {'form':form, 'mensaje':f'usuario creado:{username}'})
    else:
        form=UserRegisterForm() 
    return render(request, 'accounts/signup.html', {'form':form})

#Perfiles
@login_required
def editarPerfil(request):
    usuario=request.user #el que esta logueado...
    if request.method=='POST':
        formulario=UserEditForm(request.POST, instance=usuario) #falta crearlo en forms, o importarlo
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'accounts/inicio.html', {'usuario':usuario, 'mensaje':'TU PERFIL HA SIDO ACTUALIZADO'})
        #me esta faltando este else....osea if not is_valid...?
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'accounts/profile.html', {'formulario':formulario, 'usuario':usuario.username})
