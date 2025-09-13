from django.urls import path
from .views import registrar_equipo,detalle_equipo,listado_equipos,menu_recepcion,logout_view

urlpatterns = [
    path("", menu_recepcion, name="menu_recepcion"),
    path("registrar/", registrar_equipo, name="registrar_equipo"),
    path("detalle/<str:nombre>/", detalle_equipo, name="detalle_equipo"),
    path("listado/", listado_equipos, name="listado_equipos"),
    path("logout/", logout_view, name="logout_view"),
    
]