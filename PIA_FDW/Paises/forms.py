from django import forms
from .models import Encuesta

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'edad', 'fecha', 'telefono', 'genero', 'educacion', 'correo', 'password', 'comentarios', 'terminos']
        widgets = {
            'password': forms.PasswordInput(),  # Para mostrar el campo de password como campo oculto
        }