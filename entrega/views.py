# entrega/views.py
from django.shortcuts import render, redirect
from core import recepcion_equipos, diagnosticos, entregas

def verificar_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    
    equipo_encontrado = None
    mensaje = None

    if request.method == "GET":
        cliente = request.GET.get("cliente")
        if cliente:
            for entrega in entregas:
                if entrega["cliente"] == cliente:
                    equipo_encontrado = entrega
                    mensaje = f"Equipo para {cliente} con estado: {entrega['estado']}"
                    break

            if not equipo_encontrado:
                for recepcion in recepcion_equipos:
                    if recepcion["cliente"] == cliente:
                        equipo_encontrado = recepcion
                        mensaje = f"Equipo para {cliente} aún no tiene reporte de entrega."
                        break
            if not equipo_encontrado:
                mensaje = f"No se encontró equipo para {cliente}."

    return render(request, "entrega/verificar.html", {
        "equipo": equipo_encontrado,
        "mensaje": mensaje
    })

def reporte_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    mensaje = None
    equipo_encontrado = None

    if request.method == "POST":
        cliente = request.POST.get("cliente")
        estado = request.POST.get("estado")
        observaciones = request.POST.get("observaciones")
        if not cliente or not estado or not observaciones:
            mensaje = "Todos los campos son obligatorios."
        else:
            equipo_recepcion = None
            for recepcion in recepcion_equipos:
                if recepcion["cliente"] == cliente:
                    equipo_recepcion = recepcion
                    break

            if equipo_recepcion:
                entrega_existente = None
                for entrega in entregas:
                    if entrega["cliente"] == cliente:
                        entrega_existente = entrega
                        break

                if entrega_existente:
                    entrega_existente["estado"] = estado
                    entrega_existente["observaciones"] = observaciones
                    equipo_encontrado = entrega_existente
                    mensaje = f"Reporte de entrega actualizado: {estado}"
                else:
                    entrega = {
                        "cliente": cliente,
                        "equipo": equipo_recepcion["equipo"],
                        "problema": equipo_recepcion["problema"],
                        "estado": estado,
                        "observaciones": observaciones
                    }

                    diag = None
                    for diagnostico in diagnosticos:
                        if diagnostico["equipo"] == equipo_recepcion["equipo"]:
                            diag = diagnostico
                            break

                    if diag:
                        entrega["diagnostico"] = diag["diagnostico"]
                        entrega["solucion"] = diag["solucion"]
                        entrega["tipo"] = diag["tipo"]

                    entregas.append(entrega)
                    equipo_encontrado = entrega
                    mensaje = f"Reporte de entrega registrado: {estado}"
            else:
                mensaje = "No se encontró equipo en recepción para este cliente."
    return render(request, "entrega/reporte.html", {"mensaje": mensaje, "equipo": equipo_encontrado})

def comprobante(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    return render(request, "entrega/comprobante.html", {"entregas": entregas})
