# diagnostico/views.py
from django.shortcuts import render, redirect
from core import recepcion_equipos, diagnosticos

def evaluar_diagnostico(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    mensaje = ""
    if request.method == "POST":
        estudiante = request.POST.get("estudiante")
        equipo = request.POST.get("equipo")
        diagnostico = request.POST.get("diagnostico")
        solucion = request.POST.get("solucion")
        tipo = request.POST.get("tipo")
        if any(e["equipo"] == equipo for e in recepcion_equipos):
            diagnosticos.append({
                "estudiante": estudiante,
                "equipo": equipo,
                "diagnostico": diagnostico,
                "solucion": solucion,
                "tipo": tipo
            })
            mensaje = f"Diagnóstico registrado para {equipo}."
        else:
            mensaje = "El equipo no existe en recepción."


    return render(request, "diagnostico/evaluar.html", {"mensaje": mensaje,"recepcion_equipos": recepcion_equipos})

def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, "diagnostico/listado.html", {"diagnosticos": diagnosticos})
