import pygame
import time
from pygame.locals import *

    ALTO=600
    ANCHO=600
class Bloque(pygame,sprite.Sprite):
    def __init__(self):
        pigame.sprite.Sprite.__init__(self)

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    fin = False
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
