import pygame
import random

Alto=480
Ancho=640
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]


if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    imagen = pygame.image.load('sprite/animals.png')

    info =imagen.get_rect()
    print (info)
    an_im =info[2]
    al_im =info[3]

    an_corte=int(an_im/3)
    al_corte=int(al_im/4)
    print(an_im, an_corte, al_im, al_corte)

    y=2
    fila=[]

    for x in range(3):
        cuadro =imagen.subsurface(x*an_corte, y*al_corte, an_corte, al_corte)
        fila.append(cuadro)
        print(fila, x)


    reloj=pygame.time.Clock()
    fin=False

    i=1
    px = 0
    py = 0
    vel_x = 0
    vel_y = 0
    while not fin:
        #Gestion de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin=True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x = 0 #se pone igual a cero para que en la parte 'logica del juego' se cumpla el if y asI recorte nuevas imagenes
                    y=1
                    vel_x = -7
                    vel_y = 0
                if evento.key == pygame.K_RIGHT:
                    x = 0 #se pone igual a cero para que en la parte 'logica del juego' se cumpla el if y asi recorte nuevas imagenes
                    y=2
                    vel_x = 7
                    vel_y = 0
                if evento.key == pygame.K_UP:
                    x = 0 #se pone igual a cero para que en la parte 'logica del juego' se cumpla el if y asi recorte nuevas imagenes
                    y=3
                    vel_x = 0
                    vel_y = -7
                if evento.key == pygame.K_DOWN:
                    x = 0 #se pone igual a cero para que en la parte 'logica del juego' se cumpla el if y asi recorte nuevas imagenes
                    y=0
                    vel_x = 0
                    vel_y = 7
            if evento.type == pygame.KEYUP:
                vel_x = 0
                vel_y = 0



        #Logica del juego
        if x==0:
            for elem in fila:
                cuadro =imagen.subsurface(x*an_corte, y*al_corte, an_corte, al_corte)
                x +=1
                fila[fila.index(elem)] = cuadro
        #Refresco de pantall
        pantalla.fill(Negro)
        pantalla.blit(fila[i],[px,py])
        pygame.display.flip()
        i+=1
        if i >=3:
            i=0
        px +=vel_x
        py +=vel_y
        reloj.tick(20)
