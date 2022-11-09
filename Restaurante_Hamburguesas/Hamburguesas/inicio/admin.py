from django.contrib import admin

from .models import *

admin.site.register(Sucursal)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(TipoCarne)
admin.site.register(Hamburguesas)
admin.site.register(Bebidas)
admin.site.register(Combos)

# Register your models here.
