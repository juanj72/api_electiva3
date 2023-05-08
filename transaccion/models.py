from django.db import models
from cuenta.models import Cuenta

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

class Transaccion(models.Model):
    cuenta=models.ForeignKey(Cuenta,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True)
    monto = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_created=True,auto_now=True)