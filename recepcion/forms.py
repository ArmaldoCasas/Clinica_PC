from django import forms
from .models import Paciente

class RecepcionForm(forms.ModelForm):
    
    class Meta:
        model = Paciente 
        fields = ["cliente","equipo","problema"]
        widgets = {
            "cliente": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del Cliente"}),
            "equipo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Equipo"}),
            "problema": forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "Problema"})
        }
        error_messages = {
            "cliente": {
                "unique": "Ya existe un cliente registrado con este nombre."
            }
        }




