from django.urls import path
from .views import evaluar_diagnostico,listado_diagnosticos

urlpatterns = [
    path("evaluar_diagnostico/", evaluar_diagnostico, name="evaluar_diagnostico"),
    path("listado_diagnosticos/", listado_diagnosticos, name="listado_diagnosticos"),
]
