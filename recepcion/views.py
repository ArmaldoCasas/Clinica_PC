from django.shortcuts import render, redirect
from core import recepcion_equipos
from .models import Paciente
from .forms import RecepcionForm

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    if request.method == "POST":
        formulario_recepcion = RecepcionForm(request.POST)
        if formulario_recepcion.is_valid():
            formulario_recepcion.save()
            return redirect("registrar_equipo")    
    else:
        formulario_recepcion=RecepcionForm()
    return render(request, "recepcion/registrar.html", {"formulario_recepcion":formulario_recepcion})


def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    Pacientes = Paciente.objects.all() 
    return render(request,"recepcion/listado.html",{
        "titulo":"Listado de equipos",
        "equipos": Pacientes 
    })




def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    equipo_encontrado = None
    for e in recepcion_equipos:
        if e["cliente"] == nombre:
            equipo_encontrado = e
            break
    return render(request, "recepcion/detalle.html", {"equipo": equipo_encontrado})


def menu_recepcion(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, "recepcion/menu.html")

def logout_view(request):
    request.session.flush()
    return redirect('login_view')
# Create your views here.
