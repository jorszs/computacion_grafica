import pygame
import time
from pygame.locals import *





if __name__ == '__main__':
    #definicion de variables
    pygame.init()

    ALTO=500
    ANCHO=700
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    fondo = pygame.image.load("sprites/fondo.jpg")
    jugador = pygame.image.load("sprites/navesita.png")
    #rick = pygame.image.load("sprites/tux.png")
    #info = img.get_rect()
    #print info[2],info[3]

    #pantalla.blit(fondo,[0,0])
    pygame.display.flip()
    pos_x=-450
    pos_y=-30

    vel_x = 0
    click =False


    reloj = pygame.time.Clock()
    fin = False
    #pygame.mixer.music.load('sonidos/rick.mp3')
    #pygame.mixer.music.play(3)
    #ciclo del programa
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True

        #pygame.draw.line(pantalla,[255,0,100],[500,0],[500,ALTO],2)
        #pos_xrick += vel_x
        pantalla.blit(fondo,[pos_x,pos_y])
        pantalla.draw(jugador,[0,0])
        #pantalla.blit(rick,[pos_xrick,pos_yrick])
        #pygame.draw.line(pantalla,[255,0,100],[500,0],[500,ALTO],2)
        pygame.display.flip()
        #pos_x-=2
        reloj.tick(40)
