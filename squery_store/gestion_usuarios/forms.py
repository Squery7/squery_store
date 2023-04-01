from django import forms
from gestion_usuarios.models import Pokemon
from gestion_usuarios.models import Usuario

class PokemonForm(forms.ModelForm):
    class Meta:
        
        model = Pokemon
        fields = ['nombre', 'tipo', 'nivel', 'imagen', 'descripcion']

class RegistroForm(forms.ModelForm):
    class Meta:

        model = Usuario
        fields = ['nombre', 'apellido', 'usuario', 'email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
