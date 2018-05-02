import pygame
import math


reloj = pygame.time.Clock()
def transdepolar (punto):
    #for punto in ls_p:
    x=punto[0]*math.cos(punto[1])
    y=punto[0]*math.sin(punto[1])
    return [x,y]

def aradianes(punto):
    punt=math.radians(punto[1])
    return [punto[0],punt]

def transformacion1(centro,pto):
    pto[0] = int(centro[0] + pto[0])
    pto[1] = int(centro[1] - pto[1])
    return pto
def rosa(amplitud,num_petalos,angulo):
    r = amplitud*math.cos(num_petalos*angulo)
    return(r,angulo)

def dibujar():
    angulo=0
    while angulo <= 360:
        reloj.tick(40)
        punto_polar=rosa(200,6,math.radians(angulo))
        punto_cartesiano=transdepolar(punto_polar)
        punto_pantalla = transformacion1(centro,punto_cartesiano)
        pygame.draw.circle(pantalla,[0,255,255],punto_pantalla,3)
        pygame.draw.line(pantalla,[255,255,0],centro,punto_pantalla)
        pygame.display.flip()
        angulo+=1

def graf_lpuntos(lista):
    #lista=[]
    for punto in lista:
        n=aradianes(punto)
        np=transdepolar(n)
        np2=transformacion1(centro,np)
        pygame.draw.circle(pantalla,[0,255,255],np2,5)
#def lis_punto
if __name__ == '__main__':
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    centro=[ANCHO/2,ALTO/2]
    punto = [100,45]
    lista_puntos=[[100,45],[100,120],[100,210],[100,300]]

    #dibujar el plano cartesiano
    pygame.draw.line(pantalla,[0,255,255],[ANCHO/2,0],[ANCHO/2,ALTO])
    pygame.draw.line(pantalla,[0,255,255],[0,ALTO/2],[ANCHO,ALTO/2])

    fin = False
    #capturar los diferentes tipos de eventos
    graf_lpuntos(lista_puntos)
    pygame.display.flip()
    #   pygame.draw.polygon(pantalla,[0,255,255],listagraf,1)
    dibujar()
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
    pygame.display.flip()
