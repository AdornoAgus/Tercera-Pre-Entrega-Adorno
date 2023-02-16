from django.shortcuts import render
from django.http import HttpResponse
from mi_buloneria.models import *
from mi_buloneria.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'template/inicio.html')
