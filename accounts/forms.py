from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    #falta agregar los otros campos!!???? tipo  la info, foto, descripcion, link web, 
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields} #me pone vacios los help_texts en estos campos. 

class UserEditForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    #falta agregar los otros campos!!????  la info, foto, descripcion, link web
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields}

#formulario para usuarios:
class UsuariosForm(forms.Form):
    usuario= forms.CharField(max_length=50) #lo tengo q linkear al username?
    contrasena= forms.CharField(max_length=50) #no hay q poner ya el campo de password?
    email= forms.EmailField()
    #imagen=models.ImageField() #va con label?como el avatar? on con ForeignKey? lo dejo asi xq me pide instalar Pillow...
    descripcion= forms.CharField() #no me dejaba q sea TextField para forms....
    link= forms.URLField(max_length=200)