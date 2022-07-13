from django.db import models

# Create your models here.
class Bodega(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()

class Vino(models.Model):
    nombre=models.CharField(max_length=50)
    varietal=models.CharField(max_length=50)
    bodega=models.CharField(max_length=50)

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    pais=models.CharField(max_length=50)