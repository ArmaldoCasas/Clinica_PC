from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    
    class Meta:
        model = Estudiante 
        fields = ["estudiante","equipo","diagnostico","solucion","tipo"]
        widgets = {
            "diagnostico": forms.TextInput(attrs={"placeholder":"Diagnostico"}),
            "solucion": forms.TextInput(attrs={"placeholder":"Soolucion"}),
        }
        labels={
            "estudiante":"Nombre del Estudiante",
            "equipo":"Equipo",
            "diagnostico":"Diagnostico Realizado",
            "solucion":"Solucion a implementar",
            "tipo": "Tipo de diagnostico",

        }

