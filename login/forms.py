from django import forms
from .models import Usuario

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)
    nit = forms.CharField(max_length=20, help_text="Ingrese su número de identificación tributaria.")
    nombre = forms.CharField(max_length=100, help_text="Ingrese su nombre.")
    apellido = forms.CharField(max_length=100, help_text="Ingrese su apellido.")

    def clean_username(self):
        # Valida que el nombre de usuario no esté en uso
        username = self.cleaned_data['username']
        if Usuario.objects.filter(usuario=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
