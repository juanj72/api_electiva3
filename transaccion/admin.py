from django.contrib import admin
from transaccion.models import *
# Register your models here.
@admin.register(Transaccion)
class transaccion_admin(admin.ModelAdmin):
    list_display=['cuenta','monto','descripcion']


@admin.register(Categoria)
class categoria_admin(admin.ModelAdmin):
    list_display = ['nombre','tipo','descripcion']