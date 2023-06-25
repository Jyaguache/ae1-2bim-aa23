from django.contrib import admin
from inventario.models import Ferreteria
from inventario.models import Epp

# Agregar la clase para administrar desde
# interfaz de administración
admin.site.register(Ferreteria)
admin.site.register(Epp)