from django.shortcuts import render
equipos =[]

def registrar_equipo(request):
    mensaje = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        equipo = request.POST.get('equipo')
        problema = request.POST.get('problema')

        nuevo_equipo = {
            'nombre': nombre,
            'equipo': equipo,
            'problema': problema,
        }
        equipos.append(nuevo_equipo)

        mensaje = f"Equipo {nombre} registrado correctamente."
        return render(request, 'recepcion/registrar.html', {'mensaje': mensaje})

    return render(request, 'recepcion/registrar.html')

def listado_equipos(request):
    return render(request, 'recepcion/listado.html', {'equipos': equipos})

def detalle_equipo(request, nombre):
    equipo = None
    for e in equipos:
        if e['nombre'] == nombre:
            equipo = e
            break 
    return render(request, 'recepcion/detalle.html', {'equipo': equipo})


def menu_recepcion(request):
    return render(request, "recepcion/menu.html")



# Create your views here.
