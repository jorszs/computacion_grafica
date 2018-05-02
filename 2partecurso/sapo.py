import pygame
import random
import ConfigParser
#import time
Alto=480
Ancho=640
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]


def Recortar(nf,nc,archivo):#nf =numero de filas; nc = numero de columnas
    image=pygame.image.load(archivo)
    info=image.get_rect()
    an_img=info[2]
    al_img=info[3]
    an_corte=int(an_img/nc)
    al_corte=int(al_img/nf)
    m=[]
    for y in range(nf):
        fila=[]
        for x in range(nc):
            cuadro = image.subsurface(x*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m

if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    imagen = 'sprite/animals1.png'
    m = Recortar(4,3,imagen)


    reloj=pygame.time.Clock()
    fin=False
    accion = 2
    i=0
    pos_x=20
    pos_y=30
    vel_x = 5
    while not fin:
    #Gestion de eventos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

    #Refresco
        i+=1
        if i >=3:
            i=0

        pantalla.fill(Negro)
        pantalla.blit(m[accion][i],[pos_x,pos_y])
        pygame.display.flip()
        i+=1
        if i >=3:
            i=0
        pos_x +=vel_x
        reloj.tick(20)
