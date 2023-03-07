from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from mi_buloneria.models import *
from mi_buloneria.forms import *

# Create your views here.

def inicio(request):
    if request.GET:
        variable = request.GET['marca']
        depo_= Deposito.objects.filter(marca__icontains= variable)
        contexto = {"referencia":depo_}
        return render(request, "inicio.html", contexto)
    
    return render(request, "inicio.html",{})

def cliente(request):
    if request.method == 'POST':
        mi_formulario = Form_Cliente(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            cliente_ = Cliente(nombre=informacion['nombre'], email=informacion['mail'])
            cliente_.save()
            return render(request, "inicio.html")
        
    else:
        mi_formulario =Form_Cliente()
        
    return render(request, "cliente.html", {"mi_formulario":mi_formulario}) 
        
    

def proveedor(request):
    if request.method == 'POST':
        mi_formulario = Form_Proveedor(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            proveedor_ = Proveedor(nombre=informacion['nombre'], rubro=informacion['rubro'])
            proveedor_.save()
            return render(request, "inicio.html")
        
    else:
        mi_formulario =Form_Proveedor()
        
    return render(request, "proveedores.html", {"mi_formulario":mi_formulario})

def deposito_(request):
    if request.method == 'POST':
        mi_formulario = Form_Deposito(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            depositos_ = Deposito(item=informacion['item'], cantidad=informacion['cantidad'], marca=informacion['marca'])
            depositos_.save()
            return render(request, "inicio.html")   
    else:
       mi_formulario=Form_Deposito()
       
    return render(request, "deposito.html", {"mi_formulario":mi_formulario})



    
           
    


