# diagnostico/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Estudiante
from .forms import EstudianteForm

def evaluar_diagnostico(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    if request.method == "POST":
        formulario_diagnostico = EstudianteForm(request.POST)
        if formulario_diagnostico.is_valid():
            formulario_diagnostico.save()
            messages.success(request, "Diagnóstico registrado exitosamente.")
            return redirect("evaluar_diagnostico") 
    else:
        formulario_diagnostico=EstudianteForm()
    return render(request, "diagnostico/evaluar.html", {"formulario_diagnostico": formulario_diagnostico})

def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, "diagnostico/listado.html", {"diagnosticos": Estudiante.objects.all()})

def editar_diagnostico(request, pk):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    equipo_encontrado = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        formulario_diagnostico = EstudianteForm(request.POST, instance=equipo_encontrado)
        if formulario_diagnostico.is_valid():
            formulario_diagnostico.save()
            return redirect("listado_diagnosticos")
    else:
        formulario_diagnostico = EstudianteForm(instance=equipo_encontrado)
    return render(request, "diagnostico/evaluar.html", {"formulario_diagnostico": formulario_diagnostico})

def eliminar_diagnostico(request, pk):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    equipo_encontrado = get_object_or_404(Estudiante, pk=pk)
    equipo_encontrado.delete()
    return redirect("listado_diagnosticos")