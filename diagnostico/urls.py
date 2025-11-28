from django.urls import path
from .views import evaluar_diagnostico,listado_diagnosticos,editar_diagnostico,eliminar_diagnostico

urlpatterns = [
    path("evaluar_diagnostico/", evaluar_diagnostico, name="evaluar_diagnostico"),
    path("listado_diagnosticos/", listado_diagnosticos, name="listado_diagnosticos"),
    path("editar_diagnostico/<int:pk>/", editar_diagnostico, name="editar_diagnostico"),
    path("eliminar_diagnostico/<int:pk>/", eliminar_diagnostico, name="eliminar_diagnostico"),
]
