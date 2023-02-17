from django import forms
#f
class Form_Cliente(forms.Form):
    nombre = forms.CharField(max_length=200)
    mail = forms.EmailField()
    
  
class Form_Proveedor(forms.Form):
    nombre = forms.CharField(max_length=200)
    rubro = forms.CharField(max_length=200)

    
class Form_Deposito(forms.Form):
    item = forms.CharField(max_length=200)
    cantidad = forms.IntegerField()
    marca = forms.CharField(max_length=200)