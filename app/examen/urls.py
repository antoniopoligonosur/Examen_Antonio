from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('videojuegos-sede/<str:tituloVideojuego>/<str:paisVideojuego>',views.dame_videojuego_sede, name='dame_videojuego_sede'),
    path('videojuegos-plataforma/<str:nombreFabricante>/<str:nombrePlataforma>/<int:numeroPuntuacion>',views.dame_videojuego_plataforma, name='dame_videojuego_plataforma'),
    path('videojuegos-vd-null/',views.dame_videojuego_videojuegoPlataforma_null, name='dame_videojuego_videojuegoPlataforma_null'),
]

