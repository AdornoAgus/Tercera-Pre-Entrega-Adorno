from django.contrib import admin
from django.urls import path
from mi_buloneria import views



urlpatterns = [
    path('',views.inicio, name="inicio"),
]
