import pygame
import time

if __name__ == '__main__':
    #definicion de variables
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    img = pygame.image.load("tux.png")
    #info = img.get_rect()
    #print info[2],info[3]

    #pantalla.blit(img,[100,100])
    pygame.display.flip()
    pos_x=0
    pos_y=0
    click =False

    reloj = pygame.time.Clock()
    fin = False
    #ciclo del programa
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x = event.pos[0]
                pos_y = event.pos[1]
                click=True
                #img = pygame.image.load("tux.png")

                #pantalla.blit(img,[x,y])
                #pygame.display.flip()
                #x+=2



        #logica del ciclo

        #refresto de pto_pantalla
        #pantalla.fill([0,0,0])


        if click:
            pantalla.blit(img,[pos_x,pos_y])

        pygame.display.flip()
        pantalla.fill([0,0,0])
        pos_x+=2
        reloj.tick(30)
