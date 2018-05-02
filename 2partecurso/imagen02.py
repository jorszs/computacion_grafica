import pygame
import time
from pygame.locals import *
if __name__ == '__main__':
    #definicion de variables
    pygame.init()

    ALTO=600
    ANCHO=600
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    fondo = pygame.image.load("sprite/fondo5.jpg")
    rick = pygame.image.load("sprite/tux.png")
    #info = img.get_rect()
    #print info[2],info[3]

    #pantalla.blit(fondo,[0,0])
    pygame.display.flip()
    pos_x=0
    pos_y=0
    pos_xrick=100
    pos_yrick=400
    click =False

    reloj = pygame.time.Clock()
    fin = False
    pygame.mixer.music.load('sonidos/rick.mp3')
    pygame.mixer.music.play(3)
    #ciclo del programa
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            if pygame.mouse.get_pos()[0]>=500:
                pos_x-=2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pos_xrick+=10
                if event.key == pygame.K_LEFT:
                    pos_xrick-=10
                if event.key == pygame.K_UP:
                    pos_yrick-=10
                if event.key == pygame.K_DOWN:
                    pos_yrick+=10
            if pos_xrick >=500:
                pos_x-=10
                pos_xrick=500
            if pos_xrick <=50:
                pos_x+=10
                pos_xrick=50

        #pygame.draw.line(pantalla,[255,0,100],[500,0],[500,ALTO],2)

        pantalla.blit(fondo,[pos_x,-400])
        pantalla.blit(rick,[pos_xrick,pos_yrick])
        pygame.draw.line(pantalla,[255,0,100],[500,0],[500,ALTO],2)
        pygame.display.flip()
        #pos_x-=2
        reloj.tick(40)
