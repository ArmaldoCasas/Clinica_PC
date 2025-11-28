from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    
    class Meta:
        model = Estudiante 
        fields = ["estudiante","equipo","diagnostico","solucion","tipo"]
        widgets = {
            "estudiante": forms.TextInput(attrs={"class":"form-control","placeholder":"Estudiante"}),
            "equipo": forms.Select(attrs={"class":"form-select","placeholder":"Equipo"}),
            "diagnostico": forms.TextInput(attrs={"class":"form-control","placeholder":"Diagnostico"}),
            "solucion": forms.TextInput(attrs={"class":"form-control","placeholder":"Solucion"}),
            "tipo": forms.Select(attrs={"class":"form-select","placeholder":"Tipo"}),
        }
        labels={
            "estudiante":"Nombre del Estudiante",
            "equipo":"Equipo",
            "diagnostico":"Diagnostico Realizado",
            "solucion":"Solucion a implementar",
            "tipo": "Tipo de diagnostico",

        }

