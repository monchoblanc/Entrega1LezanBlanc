from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    #estos los saco xq sino me los pide si o si al hacer sign up. mejor q sean solo al EditarPerfil.
    #imagen=forms.ImageField() #pide instalar Pillow...
    #descripcion= forms.CharField() #no me dejaba q sea TextField para forms....
    #link= forms.URLField(max_length=200)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields} #me pone vacios los help_texts en estos campos. 

class UserEditForm(UserCreationForm):
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    #falta agregar los otros campos: foto, descripcion, link web:
    imagen=forms.ImageField() #pide instalar Pillow...
    descripcion=forms.CharField() #no me dejaba q sea TextField para forms....max length?
    link=forms.URLField(max_length=200)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields}

'''#formulario para usuarios:  UNIR ESTE CON EL DE ARRIBA!!! y despues este ya lo puedo borrar!
class UsuarioForm(forms.Form):
    usuario= forms.CharField(max_length=50) #lo tengo q linkear al username?
    contrasena= forms.CharField(max_length=50) #no hay q poner ya el campo de password?
    email= forms.EmailField()
    #imagen=forms.ImageField() #va con label?como el avatar? on con ForeignKey? lo dejo asi xq me pide instalar Pillow...
    descripcion= forms.CharField() #no me dejaba q sea TextField para forms....
    link= forms.URLField(max_length=200)'''