from django.urls import path
from .views import registrar_equipo, listado_equipos, detalle_equipo, menu_recepcion, logout_view, editar_equipo, eliminar_equipo
from .api_views import api_lista_pacientes, api_agregar_pacientes, api_modificar_pacientes, api_eliminar_pacientes
urlpatterns = [
    path('registrar/', registrar_equipo, name='registrar_equipo'), 
    path('listado/', listado_equipos, name='listado_equipos'), 
    path('detalle/<int:pk>/', detalle_equipo, name='detalle_equipo'), 
    path('menu/', menu_recepcion, name='menu_recepcion'), 
    path('logout/', logout_view, name='logout_view'), 
    path('editar/<int:pk>/', editar_equipo, name='editar_equipo'),
    path('eliminar/<int:pk>/', eliminar_equipo, name='eliminar_equipo'),
    path('api/listado/', api_lista_pacientes, name='api_lista_pacientes'),
    path('api/agregar/', api_agregar_pacientes, name='api_agregar_pacientes'),
    path('api/modificar/<int:pk>/', api_modificar_pacientes, name='api_modificar_pacientes'),
    path('api/eliminar/<int:pk>/', api_eliminar_pacientes, name='api_eliminar_pacientes'),
]
