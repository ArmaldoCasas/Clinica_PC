from django.shortcuts import render,redirect

diagnosticos = []

def asignar_diagnostico(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')

    mensaje = None

    if request.method == 'GET':
        estudiante = request.GET.get('estudiante')
        equipo = request.GET.get('equipo')
        if estudiante and equipo:
            mensaje = f"Equipo {equipo} fue asignado a {estudiante}."

        return render(request, 'diagnostico/asignar.html', {'mensaje': mensaje})

def evaluar_diagnostico(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    mensaje = ""
    
    if request.method == "POST":
        estudiante = request.POST.get('estudiante')
        equipo = request.POST.get('equipo')
        diagnostico = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        tipo = request.POST.get('tipo')

        diagnosticos.append({
            "estudiante": estudiante,
            "equipo": equipo,
            "diagnostico": diagnostico,
            "solucion": solucion,
            "tipo": tipo
        })
        mensaje = "Diagnostico registrado correctamente."
    return render(request, 'diagnostico/evaluar.html', {'mensaje': mensaje})

def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, 'diagnostico/listado.html', {"diagnosticos": diagnosticos})

# Create your views here.
