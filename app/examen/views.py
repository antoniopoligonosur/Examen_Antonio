from django.shortcuts import render
from django.views.defaults import page_not_found
from .models import *
from django.db.models import Q , Prefetch, Avg, Max, Min

# Create your views here.

def index(request):
    return render(request, 'index.html')

# URL 1

def dame_videojuego_sede(request, tituloVideojuego, paisVideojuego): 
    
    videojuego = ( 
        Videojuego.objects
        .select_related('estudio', 'sede')
        .filter(titulo=tituloVideojuego, pais=paisVideojuego)
        .all()
    ) 

    return render(request,'Lista_Videojuego.html',{'Videojuego_Mostrar':videojuego})

# URL 2

def dame_videojuego_plataforma(request, nombreFabricante, nombrePlataforma, numeroPuntuacion): 
    
    videojuego = ( 
        Videojuego.objects
        .select_related("plataforma")
        .prefetch_related('analisisVideojuego')
        .filter(analisisVideojuego__puntuacion__gt=numeroPuntuacion)
        .all()
    )

    return render(request,'Lista_Videojuego.html',{'Videojuego_Mostrar':videojuego})

# URL 3

def dame_videojuego_videojuegoPlataforma_null(request): 
    
    videojuego = (
        Videojuego.objects
        .select_related("plataforma")
        .filter(plataforma = None)
        .all()
    )

    return render(request,'Lista_Videojuego.html',{'Videojuego_Mostrar':videojuego})

# Errores
def mi_error_404(request,exception=None):
    return render(request,'error/404.html',None,None,404)

def mi_error_403(request,exception=None):
    return render(request,'error/403.html',None,None,403)

def mi_error_400(request,exception=None):
    return render(request,'error/400.html',None,None,400)

def mi_error_500(request,exception=None):
    return render(request,'error/500.html',None,None,500)