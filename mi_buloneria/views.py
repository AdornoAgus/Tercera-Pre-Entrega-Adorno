from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from mi_buloneria.models import *
from mi_buloneria.forms import *

# Create your views here.

#def inicio(request):
#    return render(request, 'template/inicio.html')

def inicio(self):
    miHtml=open("C:/Users/Admin/Desktop/bulonera_agustin/buloneria/GitHubBulo/mi_buloneria/template/inicio.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def cliente(request):
    if request.method == 'POST':
        mi_formulario = Form_Cliente(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            cliente_ = Cliente(nombre=informacion['nombre'], email=informacion['mail'])
            cliente_.save()
            return render(request, "template/inicio.html")
        
    else:
        mi_formulario =Form_Cliente()
        
    return render(request, "template/cliente.html", {"mi_formulario":mi_formulario}) 
        
    

def proveedor(self):
    miHtml=open("C:/Users/Admin/Desktop/bulonera_agustin/buloneria/GitHubBulo/mi_buloneria/template/proveedores.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def deposito_(self):
    miHtml=open("C:/Users/Admin/Desktop/bulonera_agustin/buloneria/GitHubBulo/mi_buloneria/template/deposito.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)



