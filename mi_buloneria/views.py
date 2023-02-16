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