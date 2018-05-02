import pygame
ancho=640; alto=480  #dimensiones
verde = [0,255,0] ; rojo = [255,0,0] ;negro = [0,0,0]
reloj = pygame.time.Clock()  #reloj para manejar tiempo

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    lsptos=[]
    fin=False
    cont=0


    while not fin:
        reloj.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont <= 3:
                    lsptos.append(list(event.pos))
                    cont +=1

        for p in lsptos:
            if cont == 3:
                p[0]+=1
                pantalla.fill(negro)
                pygame.draw.polygon(pantalla,verde,lsptos)
                pygame.display.flip()
