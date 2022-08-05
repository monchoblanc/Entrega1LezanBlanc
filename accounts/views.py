from django.shortcuts import render, redirect #el redirect capaz no lo uso. 
from django.http import HttpResponse
from accounts.models import * #solo es Perfil! 
from accounts.forms import *  #importo todos xq igual son pocos. 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib import messages #?? podria no usarlo pero ya esta...
# Create your views here.

#vista home de accounts: hace falta?
def inicio(request):   
    return render(request, 'accounts/inicio.html')


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

#registro. Obs: solo guarda en model User.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username'] 
            email=form.cleaned_data['email'] #medio al pedo me estoy guardando email y contrasena aca, xq no tengo q hacer authenticate.
            contrasena=form.cleaned_data['password1'] 
            form.save()
            return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'usuario creado:{username} AHORA LOGUEATE!' })
    else:
        form=UserRegisterForm() 
    return render(request, 'accounts/signup.html', {'form':form})
    

@login_required
#@transaction.atomic. hace q se guarden ambos objetos o ninguno... (por si alguno falla, q el otro no se actualice)
def update_perfil(request): #notar q no me pide 2 veces el pswd!, x usar el ModelForm, me parece mejor!.
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user) #cambio UserForm por UserEditForm
        perfil_form = PerfilForm(request.POST, instance=request.user.perfil) 
        #uso ambos forms en la misma vista!:
        if user_form.is_valid() and perfil_form.is_valid():
            usuario=user_form.save()  #me guardo usuario asi lo paso por contexto..
            perfil_form.save()
            #messages.success(request, 'TU PERFIL HA SIDO ACTUALIZADO!') 
            return render(request, 'accounts/inicio.html', {'usuario':usuario, 'mensaje':'TU USUARIO HA SIDO ACTUALIZADO'})#redirect('settings:profile')
        else:
            messages.error(request, 'Fijate este error!:') #tmb podria pasarle return render(...mensage)
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilForm(instance=request.user.perfil)
    return render(request, 'accounts/profile.html', {'user_form': user_form, 'perfil_form': perfil_form })

'''#rompe en perfil.save()NO LE SACO LA FICHA. 
#intento crear una vista de registro q junte ambos forms!, el UserRegisterForm y el PerfilForm!:
@login_required #podria no tenerlo xq desde aca tmb podria crear un nuevo usuario...creo. 
def registerPerfil(request): #en realidad es mas un editPerfil........
    usuario=request.user
    if request.method == 'POST': 
        form = UserEditForm(request.POST, instance=usuario) #el q uso para editarUsuario, model User.
        perfil_form = PerfilForm(request.POST) #el q uso para el crear, model Perfil
        if form.is_valid() and perfil_form.is_valid(): 
            informacion=form.cleaned_data
            info_perfil=perfil_form.cleaned_data
            usuario.username=informacion['username']
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save() #guardo el de User primero! o es usuario=form.save()?
        #ahora linkeo el campo user, q es el OneToOne:
            #perfil = perfil_form.save(commit=False) #????
            descripcion=info_perfil['descripcion']
            link= info_perfil['link']
            imagen= info_perfil['imagen']
            perfil=Perfil( user=usuario , imagen=imagen, descripcion=descripcion, link=link)  
            perfil.save() # ROMPE ACA!! xq???
            return render(request, 'accounts/registerPerfil.html', {'form':form, 'perfil_form':perfil_form,'mensaje':'TU PERFIL HA SIDO ACTUALIZADO'})
    else:
        form=UserEditForm() 
        perfil_form=PerfilForm() 
    
    return render(request, 'accounts/registerPerfil.html', {'form': form, 'perfil_form': perfil_form}) # o lo mando a otro lade q /profile??'''


#vista para eliminar usuario.
@login_required
def deleteUser(request, usuario):#esta vista ponerla como un BOTON en /profile.html 
    usu=request.user 
    usu.delete()
    return render(request, 'accounts/signup.html', {'mensaje':'Su usuario ha sido eliminado'}) #si se elimina, lo mando al signup.

