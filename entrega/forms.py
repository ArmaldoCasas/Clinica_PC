from django import forms
from .models import ReporteEntrega

class EntregaForm(forms.ModelForm):
    
    class Meta:
        model = ReporteEntrega 
        fields = ["cliente","equipo","problema","estado","observacion"]
        widgets = {
            "estado": forms.TextInput(attrs={"placeholder":"estado"}),
            "observacion": forms.TextInput(attrs={"placeholder":"observacion"}),
        }
        labels={
            "cliente":"Nombre del paciente",
            "equipo":"Equipo",
            "diagnostico":"Diagnostico Realizado",
            "solucion":"Solucion a implementar",
            "observacion": "Observacion Realizada",

        }