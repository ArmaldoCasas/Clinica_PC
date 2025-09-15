from django.shortcuts import render, redirect
from core import recepcion_equipos

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    mensaje = None
    if request.method == "POST":
        cliente = request.POST.get("cliente")
        equipo = request.POST.get("equipo")
        problema = request.POST.get("problema")
        if not cliente or not equipo or not problema:
            mensaje = "Todos los campos son obligatorios. Por favor, complete cliente, equipo y problema."
        else:
            recepcion_equipos.append({
                "cliente": cliente,
                "equipo": equipo,
                "problema": problema
            })
            mensaje = f"Equipo {equipo} registrado para {cliente}."
    return render(request, "recepcion/registrar.html", {"mensaje": mensaje})

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, "recepcion/listado.html", {"equipos": recepcion_equipos})

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
