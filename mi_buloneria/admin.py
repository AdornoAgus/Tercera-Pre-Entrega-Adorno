from django.contrib import admin
from .models import Cliente, Proveedor, Deposito

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Deposito)