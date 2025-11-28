from django.urls import path
from .views import verificar_entrega,reporte_entrega,comprobante,editar_reporte,eliminar_reporte

urlpatterns = [
    path("verificar_entrega/", verificar_entrega, name="verificar_entrega"),
    path("reporte_entrega/", reporte_entrega, name="reporte_entrega"),
    path("comprobante/", comprobante, name="comprobante"),
    path("editar_reporte/<int:pk>/", editar_reporte, name="editar_reporte"),
    path("eliminar_reporte/<int:pk>/", eliminar_reporte, name="eliminar_reporte"),
]