from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nit", "nombre", "direccion", "telefono"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nit'].error_messages = {'unique': 'El NIT ingresado ya existe. Ingresa otro.'}
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


