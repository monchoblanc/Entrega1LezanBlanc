from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario= models.CharField(max_length=50) #lo tengo q linkear al username?
    contrasena= models.CharField(max_length=50) #no hay q poner ya el campo de password?
    email= models.EmailField()
    #imagen=models.ImageField() #va con label?como el avatar? on con ForeignKey? lo dejo asi xq me pide instalar Pillow...
    descripcion= models.TextField() #como cambio a ckeditor?default es Textarea...
    link= models.URLField(max_length=200) 

    def __str__(self):
        return self.usuario+'  '+self.contrasena+'  '+str(self.email) #agregar los q faltan