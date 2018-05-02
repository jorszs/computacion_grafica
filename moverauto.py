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
    fin = False
    a=[100,100]
    b=[100,300]
    lista=[]
    cont=0
    lptos=[]
    #lptos.append(a)
    #lptos.append(b)

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                sg = pygame.mouse.get_pos()
                lista.append([sg[0],sg[1]])

        if cont==3:
            for v in lista:
                v[0]+=1
                pantalla.fill([0,0,0])
                pygame.draw.polygon(pantalla, [0, 255, 0], lista)
                pygame.display.flip()
