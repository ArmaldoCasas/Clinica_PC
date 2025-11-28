from django.shortcuts import render, redirect,get_object_or_404
from .models import Paciente
from .forms import RecepcionForm
from django.contrib import messages

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    if request.method == "POST":
        formulario_recepcion = RecepcionForm(request.POST)
        if formulario_recepcion.is_valid():
            formulario_recepcion.save()
            messages.success(request, "Equipo registrado exitosamente.")
            return redirect("registrar_equipo")    
    else:
        formulario_recepcion=RecepcionForm()
    return render(request, "recepcion/registrar.html", {"formulario_recepcion":formulario_recepcion,})


def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    Pacientes = Paciente.objects.all() 
    return render(request,"recepcion/listado.html",{
        "titulo":"Listado de equipos",
        "equipos": Pacientes 
    })

def detalle_equipo(request, pk):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    equipo_encontrado = get_object_or_404(Paciente, pk=pk)
    return render(request, "recepcion/detalle.html", {"equipo": equipo_encontrado})


def editar_equipo(request, pk):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    equipo_encontrado = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        formulario_recepcion = RecepcionForm(request.POST, instance=equipo_encontrado)
        if formulario_recepcion.is_valid():
            formulario_recepcion.save()
            return redirect("listado_equipos")
    else:
        formulario_recepcion = RecepcionForm(instance=equipo_encontrado)
    return render(request, "recepcion/registrar.html", {"formulario_recepcion": formulario_recepcion})

def eliminar_equipo(request, pk):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    equipo_encontrado = get_object_or_404(Paciente, pk=pk)
    equipo_encontrado.delete()
    return redirect('listado_equipos')






def menu_recepcion(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, "recepcion/menu.html")

def logout_view(request):
    request.session.flush()
    return redirect('login_view')
# Create your views here.
