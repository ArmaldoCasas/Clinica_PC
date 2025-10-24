from django import forms
from .models import Paciente

class RecepcionForm(forms.ModelForm):
    
    class Meta:
        model = Paciente 
        fields = ["cliente","equipo","problema"]
        widgets = {
            "problema": forms.Textarea(attrs={"rows":2})
        }




