#gotas
import pygame
ancho=600; alto=500  #dimensiones
verde = [0,255,0]
reloj = pygame.time.Clock()  #reloj para manejar tiempo

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    fin = False
    lista = []

    while not fin:

        for e in lista:
            if e[1] <= alto:
                e[1] += 1
                pantalla.fill([0,0,0])
                pygame.draw.circle(pantalla,verde,e,15,5)
                pygame.display.flip()
                reloj.tick(1000)

        for evento in pygame.event.get():

            if evento.type == pygame.MOUSEBUTTONDOWN:
                punto = evento.pos; x = punto[0]  ; y =punto[1]
                pun = [x,y]
                lista.append(pun)

            if evento.type == pygame.QUIT:
                fin = True
