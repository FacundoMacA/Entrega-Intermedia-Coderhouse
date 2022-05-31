from django.urls import path
from AppDjango import views

urlpatterns = [
    path('', views.inicio, name="index"),
    path('torneos/', views.torneos_index, name="torneos"),
    path('agregar/', views.agregar_torneo, name="agregar_torneo"),
    path('borrar/<identificador>', views.borrar_torneo, name="borrar_torneo"),
    path('buscar/', views.buscar_torneo, name="buscar_torneo"),
    path('equipos/', views.equipos_index, name="equipos"),
    path('agregar_equipo/', views.agregar_equipo, name="agregar_equipo"),
    path('borrar_equipo/<identificador>', views.borrar_equipo, name="borrar_equipo"),
    path('buscar_equipo/', views.buscar_equipo, name="buscar_equipo"),
     path('jugadores/', views.jugadores_index, name="jugadores"),
    path('agregar_jugador/', views.agregar_jugador, name="agregar_jugador"),
    path('borrar_jugador/<identificador>', views.borrar_jugador, name="borrar_jugador"),
    path('buscar_jugador/', views.buscar_jugador, name="buscar_jugador"),
]
