from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('videojuegos-sede/<str:tituloVideojuego>/<str:paisVideojuego>',views.dame_videojuego_sede, name='dame_videojuego_sede'),
]

