# diagnostico/views.py
from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm
def evaluar_diagnostico(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    if request.method == "POST":

        formulario_diagnostico = EstudianteForm(request.POST)
        if formulario_diagnostico.is_valid():
            formulario_diagnostico.save()
            return redirect("evaluar_diagnostico.html") 
           
    else:
        formulario_diagnostico=EstudianteForm()
    return render(request, "diagnostico/evaluar.html", {"formulario_diagnostico": formulario_diagnostico})

def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, "diagnostico/listado.html", {"diagnosticos": Estudiante.objects.all()})