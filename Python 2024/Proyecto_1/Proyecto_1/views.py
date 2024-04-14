import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Template, Context, RequestContext
import datetime
from .models import dbo_alumnos

def pagina(request):
    return HttpResponse("Hello World DJANGO")


def paginaDatosPersonales(request):
    # nombre="José Domingo Santillán Rodríguez"
    lenguajes = "Java", "Python", "C", "C#", "R"
    datos = {
        "nombre": "José Domingo Santillán Rodríguez",
        "edad": 20,
        "fecha": datetime.datetime.now(),
        "lenguajes": lenguajes
    }
    doc_externo = open("C:/Users/MSI PRENDAMEX/Documents/Python/Python 2024/Proyecto_1/Proyecto_1/DatosEmpleado.html")
    plantilla = Template(doc_externo.read())
    cxt = Context(datos)
    data = plantilla.render(cxt)
    return HttpResponse(data)


def operacionesBasicas(request):
    operaciones = "Suma", "Resta", "Multiplicacion", "División"
    doc_externo = open(
        "C:/Users/MSI PRENDAMEX/Documents/Python/Python 2024/Proyecto_1/Proyecto_1/operacionesBasicas.html")
    plantilla = Template(doc_externo.read())
    cxt = Context()
    data = plantilla.render(cxt)
    return HttpResponse(data)


def formularios(request):
    doc_externo = open("C:/Users/MSI PRENDAMEX/Documents/Python/Python 2024/Proyecto_1/Proyecto_1/formularios.html")
    plantilla = Template(doc_externo.read())
    cxt = Context()
    data = plantilla.render(cxt)
    return HttpResponse(data)


def captura(request):
    doc_externo = open("C:/Users/MSI PRENDAMEX/Documents/Python/Python 2024/Proyecto_1/Proyecto_1/captura.html")
    plantilla = Template(doc_externo.read())
    cxt = RequestContext(request)  # Usa RequestContext aquí
    data = plantilla.render(cxt)
    return HttpResponse(data)


def informacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('inputName')
        apellido_pa = request.POST.get('inputApellidoPaterno')
        apellido_ma = request.POST.get('inputApellidoMaterno')
        fecha = request.POST.get('inputFechaNac')
        carrera = request.POST.get('carreras')
        sexo = request.POST.get('sexo')

        if not all([nombre, apellido_pa, apellido_ma, fecha, carrera, sexo]):
            return HttpResponseBadRequest('Debes insertar todos los datos')

        nuevo_usuario = dbo_alumnos(
            nombre=nombre,
            apellido_pa=apellido_pa,
            apellido_ma=apellido_ma,
            fecha_nacimiento=fecha,
            carrera=carrera,
            sexo=sexo
        )
        nuevo_usuario.save()

        doc_externo = open("C:/Users/MSI PRENDAMEX/Documents/Python/Python 2024/Proyecto_1/Proyecto_1/informacion.html")
        plantilla = Template(doc_externo.read())
        cxt = Context({'nombre': nombre, 'apellido_pa': apellido_pa, 'apellido_ma': apellido_ma, 'fecha': fecha,
                       'carrera': carrera, 'sexo': sexo})
        data = plantilla.render(cxt)
        return HttpResponse(data)
    else:
        return HttpResponseBadRequest('Se esperaba una solicitud POST')
