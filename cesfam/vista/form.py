from django import forms
from django.forms import widgets
from .models import *
from localflavor.cl.forms import *


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        labels = {
            'nombre': 'nombre completo',
        }


"""
class citaForm(forms.ModelForm):
    class Meta:
        model = cita
        fields = '__all__'
        widgets={ 'fecha':forms.DateTimeInput(attrs={'type':'datetime-local'})}

"""

