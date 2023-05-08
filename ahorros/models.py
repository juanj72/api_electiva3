from django.db import models
from cuenta.models import Cuenta
# Create your models here.


class Ahorro(models.Model):
    cuenta=models.ForeignKey(Cuenta,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    monto_obj=models.IntegerField()
    fecha_fin=models.DateTimeField()
    create_at=models.DateTimeField(auto_now=True,auto_created=True)
    