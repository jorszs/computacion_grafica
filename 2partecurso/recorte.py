import pygame
import time
import random
#definicion de variables


ALTO=600
ANCHO=600
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]


if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    #imagen = pygame.image.load("terrenogen.png")
    imagen = pygame.image.load("sprite/.png")
    #info = imagen.get_rect()
    info_s = imagen.get_rect()
    print info_s
    #an_img = info[2]#imagen.rect.width
    #al_img = info[3]#imagen.get_rect.hei
    an_img_s = info_s[2]
    al_img_s = info_s[3]

    #an_corte = int(an_img/32) #ancho imagen dividido numero de imagenes en la horizontal
    #al_corte = int(al_img/12)
    an_corte = int(an_img_s/8)
    al_corte = int (al_img_s/5)
    #x=5
    #y=3

    #cuadro = imagen.subsurface(28*32,32*6,32,32)
    #cuadrado_s = imagen.subsurface(0,0,an_corte,al_corte)

    y = 1
    fila=[]
    for x in range(6):
        cuadrado = imagen.subsurface(x*an_corte,y*al_corte,an_corte, al_corte)
        fila.append(cuadrado)


    reloj = pygame.time.Clock()
    fin = False

    i=0
    px = 0
    vel_x = 1
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True

        #logica del juego
        #refresco de pantalla
        pantalla.fill(Negro)
        pantalla.blit(fila[i],[px,0])
        pygame.display.flip()
        i+=1
        if i>= 5:
            i=0
        px += vel_x
        reloj.tick(20)
