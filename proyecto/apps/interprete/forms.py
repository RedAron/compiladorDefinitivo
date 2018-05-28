from django import forms
from .models import Programa

class programaForm(forms.ModelForm):
    class Meta:
        model=Programa
        fields=[
                'nombre',
                'script',
            ]
        labels = {
                'nombre' : 'Nombre de programa',
                'script' : 'script',
            }