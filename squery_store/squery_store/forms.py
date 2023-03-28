from django import forms
from gestion_usuarios.models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        
        model = Pokemon
        fields = ['nombre', 'tipo', 'nivel', 'imagen', 'descripcion']