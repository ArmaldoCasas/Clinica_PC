from django.urls import path
from .views import verificar_entrega,reporte_entrega,comprobante

urlpatterns = [
    path("verificar_entrega/", verificar_entrega, name="verificar_entrega"),
    path("reporte_entrega/", reporte_entrega, name="reporte_entrega"),
    path("comprobante/", comprobante, name="comprobante"),
]