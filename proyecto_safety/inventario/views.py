from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from inventario.models import *

# Create your views here.

def listar(request):
    """
        Listar los registros del modelo Ferreteria,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # Ferreteria
    ferreterias = Ferreteria.objects.all()
    # se obtiene el número de elementos de la lista
    numero_ferreterias = len(ferreterias)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'ferreterias': ferreterias, 'numero_ferreterias': numero_ferreterias}
    return render(request, 'listar_ferreteria.html', informacion_template)

    epps = Epp.objects.all()
    numero_epps = len(epps)
    informacion_template = {'epps': epps, 'numero_epps': numero_epps}
    return render(request, 'listar_epp.html', informacion_template)