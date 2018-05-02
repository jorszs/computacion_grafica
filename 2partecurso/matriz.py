import pygame
import random

Alto=480
Ancho=640
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]

def recortar(ancho,alto,limites):
    i = 0
    for y in range(ancho):
        #limites[i]
        for x in range(limites[i]):
            cuadro = imagen.subsurface(x*an_corte, y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
            i += 1
        matriz.append(fila)
        
    return matriz



if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    imagen = pygame.image.load('hero.png')
    info =imagen.get_rect()
    print (info)
    an_im =info[2]
    al_im =info[3]

    an_corte=int(an_im/8)
    al_corte=int(al_im/5)

    x = 0
    y = 0
    fila = []
    matriz = []
    limites = [8,6,6,7,2]
    '''for y in range(5):
        for x in range(8):
            cuadro = imagen.subsurface(x*an_corte, y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        matriz.append(fila)'''


    m = recortar(8,5,limites)
    reloj=pygame.time.Clock()
    fin=False

    i=0
    px = 0
    vel_x =1
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pantalla.fill(Negro)
        pantalla.blit(m[1][i],[px,0])
        pygame.display.flip()
        i+=1
        if i >=6:
            i=0
        px +=vel_x
        reloj.tick(5)
