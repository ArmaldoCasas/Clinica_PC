# entrega/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ReporteEntrega
from .forms import EntregaForm
from .forms import ReporteBusquedaForm 
from .models import ReporteEntrega

def verificar_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    formulario_busqueda = ReporteBusquedaForm()
    reporte_resultado = None
    if request.method == "POST":
        formulario_busqueda = ReporteBusquedaForm(request.POST)
        if formulario_busqueda.is_valid():
            paciente_seleccionado = formulario_busqueda.cleaned_data['paciente_a_buscar']
            try:
                #Validar que el paciente exista
                reporte = ReporteEntrega.objects.select_related('paciente').get(paciente=paciente_seleccionado)
                reporte_resultado = {
                    'existe': True,
                    'paciente': reporte.paciente,
                    'estado': reporte.estado,
                    'observaciones': reporte.observaciones,
                }
            except ReporteEntrega.DoesNotExist:
                #Validar que el paciente no exista de paso el doesnotexist hace que la pagina
                #no deje de funcionar
                reporte_resultado = {
                    'existe': False,
                    'paciente': paciente_seleccionado
                }
    return render(request, "entrega/verificar.html", {
        "formulario_busqueda": formulario_busqueda,
        "reporte_resultado": reporte_resultado
    })

def reporte_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    if request.method == "POST":
        formulario_entrega = EntregaForm(request.POST)
        if formulario_entrega.is_valid():
            formulario_entrega.save()
            messages.success(request, "Reporte guardado exitosamente")
            return redirect("reporte_entrega")
    else:
        formulario_entrega = EntregaForm()
    return render(request, "entrega/reporte.html", {"formulario_entrega": formulario_entrega})

def comprobante(request):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    entregas = ReporteEntrega.objects.all()
    return render(request, "entrega/comprobante.html", {"entregas": entregas})

def editar_reporte(request, pk):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    reporte = get_object_or_404(ReporteEntrega, pk=pk)
    if request.method == "POST":
        formulario_entrega = EntregaForm(request.POST, instance=reporte)
        if formulario_entrega.is_valid():
            formulario_entrega.save()
            return redirect("comprobante")
    else:
        formulario_entrega = EntregaForm(instance=reporte)
    return render(request, "entrega/reporte.html", {"formulario_entrega": formulario_entrega})

def eliminar_reporte(request, pk):
    if not request.session.get('autenticado'):
        return redirect('login_view')
    reporte = get_object_or_404(ReporteEntrega, pk=pk)
    reporte.delete()
    return redirect('comprobante')