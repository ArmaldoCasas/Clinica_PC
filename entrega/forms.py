from django import forms
from .models import ReporteEntrega
from recepcion.models import Paciente


class EntregaForm(forms.ModelForm):
    
    class Meta:
        model = ReporteEntrega 
        fields = ["paciente", "estado", "observaciones"]
        widgets = {
            "estado": forms.Select(attrs={"class": "form-control"}),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Observaciones"}),
            "paciente": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "paciente": "Paciente",
            "estado": "Estado de la Entrega",
            "observaciones": "Observaciones",
        }
class ReporteBusquedaForm(forms.Form):
    paciente_a_buscar = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )