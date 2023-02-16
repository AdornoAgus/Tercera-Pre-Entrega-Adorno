from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    mail = models.EmailField(blank=True)
    
    def __str__(self):
        return f"El cliente {self.nombre} ha sido registrado en la base de datos" 


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    rubro = models.CharField(max_length=200)

    def __str__(self):
        return f"El proveedor {self.nombre} ha sido registrado en la base de datos" 



class Deposito(models.Model):
    item = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=0)
    marca = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Se han guardado {self.item} del item {self.item} ha sido registrado dentro de la base de datos" 





