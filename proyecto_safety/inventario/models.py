from django.db import models

# Create your models here.
class Ferreteria(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    stock = models.IntegerField()
    
    def __str__(self):
        return """Nombre: %s - Tipo: %s \n
                Stock: %d""" % (self.nombre,
                self.tipo,
                self.stock)

class Epp(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    stock = models.IntegerField()
    
    def __str__(self):
        return """Nombre: %s - Tipo: %s \n
                Stock: %d""" % (self.nombre,
                self.tipo,
                self.stock)