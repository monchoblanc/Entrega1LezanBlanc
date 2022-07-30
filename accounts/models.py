from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario= models.CharField(max_length=50)
    contrasena= models.CharField(max_length=50) #no hay q poner ya el campo de password?
    email= models.EmailField()