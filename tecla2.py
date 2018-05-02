import pygame
import math
#Dibuja triangulo y lo escala con el teclado
ANCHO=600
ALTO=480
pto =[100,100]
verde = [0,255,0]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #o=[ANCHO/2, ALTO/2]
    #dibujarPlano(o, pantalla)
    pygame.display.flip()
    print 'Funciona'
    cont=0
    vel_y = 0
    vel_x = 0
    lista=[]
    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                lista.append(mostrarPos())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    vel_y =-1

                if event.key==pygame.K_RIGHT:
                    vel_x = 1

                if event.key==pygame.K_LEFT:
                    vel_x =-1

                if event.key == pygame.K_DOWN:
                    vel_y=1
        if (pto[1]>ALTO):
            pto[1]=ALTO-5
            vel_y=0
        else:
            pto[1]+=vel_y

        if(pto[1]<0):
            pto[1]= 0+5
            vel_y=0
        else:
            pto[1]+=vel_y
        if pto[0]>ANCHO:
            pto[0]=ANCHO-5
            vel_x=0
        else:
            pto[0]+=vel_x
        if pto[0]<0:
            pto[0]=0+5
            vel_x=0
        else:
            pto[0]+=vel_x
        pantalla.fill([0,0,0])
        pygame.draw.line(pantalla,verde,[ANCHO/2,0],[ANCHO/2,ALTO])
        pygame.draw.circle(pantalla,verde,pto,5)
        pygame.display.flip()
