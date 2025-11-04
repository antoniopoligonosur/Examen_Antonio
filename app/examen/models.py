from django.db import models

# Create your models here.

#------------------------------- SEDE ------------------------------------------ 
class Sede(models.Model):

    pais= models.CharField(max_length=30)
    
#------------------------------- ESTUDIO ------------------------------------------ 
class Estudio(models.Model):

    nombre_estudio= models.CharField(max_length=30)
    
    #1:N con sede
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='estudioSede')
    
#------------------------------- PLATAFORMA ------------------------------------------ 
class Plataforma(models.Model):

    FABRICANTES = [ 
        ('S', 'Sony'), 
        ('N', 'Nintendo'), 
        ('F', 'Fabricante3'),
    ]
    fabricante = models.CharField(max_length=1, choices=FABRICANTES) 
    nombre= models.CharField(max_length=30)

#------------------------------- VIDEOJUEGO ------------------------------------------ 
class Videojuego(models.Model): 

    titulo= models.CharField(max_length=30)
    ventas_estimadas= models.PositiveIntegerField()

    # 1:N CON ESTUDIO
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='videojuegoEstudio')
    # N:N CON PLATAFORMA
    plataforma = models.ManyToManyField(Plataforma, related_name='videojuegoPlataformas') 

#------------------------------- Analisis ------------------------------------------ 
class Analisis(models.Model):
    
    puntuacion= models.PositiveIntegerField()
    anyo_analisis= models.PositiveIntegerField()
    nombre_critico= models.CharField(max_length=30)
    
    #1:N con videojuego
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, related_name='analisisVideojuego')