from django.contrib import admin
from django.urls import path, include
from mi_buloneria import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',include('mi_buloneria.urls')),
]

