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

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
          #Gestion de eventos
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  fin=True
          
