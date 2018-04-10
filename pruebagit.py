import pygame

if __name__ == '__main__':
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    centro=[ANCHO/2,ALTO/2] #el centro del plano cartesiano

    ls_p=[] #va a guardar la lista de puntos ya escalados,para dibujarlos

    #dibuja el plano cartesiano
    pygame.draw.line(pantalla,[0,255,255],[ANCHO/2,0],[ANCHO/2,ALTO])
    pygame.draw.line(pantalla,[0,255,255],[0,ALTO/2],[ANCHO,ALTO/2])
    pygame.display.flip()

    lista_clicks=[]# se guardara la posicion de cada click

    cont = 0
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            if event.type == pygame.K_UP:
                pass    
