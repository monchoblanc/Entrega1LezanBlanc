from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import * #VER SI LOS NECESITO AL AVANZAR EN ESTAS VISTAS
from accounts.forms import *  #importo todos xq igual son pocos. 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

#vista home de accounts: hace falta?
def inicio(request):   
    return render(request, 'accounts/inicio.html')

def usuario(request): #esta era para probar, xq rompe en admin/accounts/usuario...?
    return render(request, 'accounts/usuario.html')

#login. 
def login_request(request):
    #aagregar q si ya estoy logueado no entre??, muestre cartel"ya estas logueado", y me mande a donde estaba.(igual el boton ya esto ok login/logout)
    if request.method=='POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= request.POST['username'] 
            clave= request.POST['password'] 
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
            email=form.cleaned_data['email']
            contrasena=form.cleaned_data['password1'] #rompe? es necesaria esta linea?
            form.save()
            return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'usuario creado:{username} AHORA LOGUEATE!' })
    else:
        form=UserRegisterForm() 
    return render(request, 'accounts/signup.html', {'form':form})
    

#edicion de Perfiles
@login_required
def editarPerfil(request): 
    usuario=request.user #el que esta logueado...
    if request.method=='POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.username=informacion['username']
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            # y los otros items: image, link, descripcion:
            usuario.imagen=informacion['imagen']
            usuario.descripcion=informacion['descripcion']
            usuario.link=informacion['link']
            usuario.save()
            return render(request, 'accounts/inicio.html', {'usuario':usuario, 'mensaje':'TU PERFIL HA SIDO ACTUALIZADO'})
        #me esta faltando este else....osea if not is_valid...?
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'accounts/profile.html', {'formulario':formulario, 'usuario':usuario.username}) #lo mando a /profile. xq ahi lo pide la consigna. queda raro, pero es para q sea en esa ruta.. 


#vista para eliminar usuario. NO estoy seguro si era un requisito en consignas, o solo el edit. 
@login_required
def eliminarUsuario(request, usuario):#esta vista ponerla como un BOTON en /profile.html
#no estoy seguro si esta ok como estoy llamando al usuario. tendria q ser request.user pero me chilla. 
    usu=request.user 
    usu.delete()
    return render(request, 'accounts/login.html', {'mensaje':'Su usuario ha sido eliminado'}) #si se elimina, me manda al login.