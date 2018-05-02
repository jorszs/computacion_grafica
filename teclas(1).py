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
                    print 'arriba'
                    if(pto[1] == 0):
                        print 'no se puede avanzar'
                    else:
                        pto[1]-=2
                if event.key == pygame.K_a:
                    print 'a'

                if event.key==pygame.K_RIGHT:
                    if(pto[0] == 200):
                        print 'no se puede avanzar'
                    else:
                        pto[0]+=2


                if event.key==pygame.K_LEFT:
                    if(pto[0] == 0):
                        print 'no se puede avanzar'
                    else:
                        pto[0]-=2

                if event.key == pygame.K_DOWN:
                    pto[1]+=2
            pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,verde,pto,5)
        pygame.display.flip()
