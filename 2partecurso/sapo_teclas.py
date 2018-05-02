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

#recorta el sprite y queda almacenado en una matriz(lista de listas)
#ej:para un sprite de 2x2 matriz=[[cuadro1fila1,cuadro2fila],[cuadro1fila2,cuadro2fila2]]
def Recortar(nf,nc,archivo):#nf =numero de filas; nc = numero de columnas
    image=pygame.image.load(archivo)
    info=image.get_rect()
    an_img=info[2]
    al_img=info[3]
    an_corte=int(an_img/nc)#ancho de cada figura en este caso del sapo
    al_corte=int(al_img/nf)#ancho de cada figura en este caso del sapo
    m=[]#matriz donde quedara almacenados las figuras del sprite ya recortadas
    for y in range(nf): #recorre todas las filas del sprite
        fila=[]#permite que cada ciclo esta lista esta vacia
        for x in range(nc):#recorre todas las columnas del sprite de cada fila
            cuadro = image.subsurface(x*an_corte,y*al_corte,an_corte,al_corte)#recorta cada figura (cada sapo)
            fila.append(cuadro)#agrega cada figura a una lista
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

    i=0
    accion = 0 #basicamente es el numero de fila que quiero utilizar de la matriz
    #accion 0 es que el sapo se mueva hacia abajo 
    pos_x=20
    pos_y=30
    vel_x = 0
    vel_y = 0
    while not fin:
    #Gestion de eventos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vel_y = 0
                    accion = 1
                    vel_x = -5
                if event.key == pygame.K_RIGHT:
                    vel_y = 0
                    print 'espacio'
                    accion = 2
                    vel_x = 5
                if event.key == pygame.K_DOWN:
                    vel_x = 0
                    print 'espacio'
                    accion = 0
                    vel_y = 5
                if event.key == pygame.K_UP:
                    vel_x = 0
                    print 'espacio'
                    accion = 3
                    vel_y = -5
    #Refresco

        pantalla.fill(Negro)
        pantalla.blit(m[accion][i],[pos_x,pos_y])#dibuja el movimiento del sprite(sapo) en las cordenadas pos_x y pos_y
        pygame.display.flip()
        i+=1     #permite que por cada accion
        if i >=3:#la funcion pantalla.blit (justo arriba)
            i=0  #recorra la lista de imagenes en la matriz m que componen a cada accion

        pos_x += vel_x
        pos_y += vel_y
        reloj.tick(5)
