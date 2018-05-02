import pygame
import random

Alto=480
Ancho=640
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]

def Recortar(nf,nc,archivo,limites):
    image=pygame.image.load(archivo)
    info=image.get_rect()
    an_img=info[2]
    al_img=info[3]
    an_corte=int(an_im/nc)
    al_corte=int(al_im/nf)
    m=[]
    for y in range(nf):
        fila=[]
        for x in range(limites[y]):
            cuadro = image.subsurface(x*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m


if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    imagen = pygame.image.load('sprite/animals1.png')

    info =imagen.get_rect()
    print (info)
    an_im =info[2]
    al_im =info[3]
    limites=[3,3,3,3]

    an_corte=int(an_im/3)
    al_corte=int(al_im/4)
    print(an_im,an_corte,al_im,al_corte)

    #matriz de la imagen
    m = Recortar(an_im,al_im,'sprite/animals1.png',limites)

    y=2
    fila=[]
    for x in range(3):
        cuadro =imagen.subsurface(x*an_corte, y*al_corte, an_corte, al_corte)
        fila.append(cuadro)


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pass


        #Logica del juego
        #Refresco de pantall
        pantalla.fill(Negro)
        pantalla.blit(fila[i],[px,0])
        pygame.display.flip()
        i+=1
        if i >=3:
            i=0
        px +=vel_x
        reloj.tick(5)
