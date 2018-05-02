
import pygame

if __name__ == '__main__':
    pygame.init()
    print 'probando...'
    pantalla = pygame.display.set_mode([600,480])
    pygame.draw.line(pantalla,[255,0,0],[100,100],[200,100])
    pygame.display.flip()
    con = 0

    fin=False
    lista_puntos=[]

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print 'click'
                con+=1
                lista_puntos.append(event.pos)
                if con==2:
                    #pos2=event.pos
                    pygame.draw.line(pantalla,[255,0,0],lista_puntos[0],lista_puntos[1])
                    pygame.display.flip()
                    con = 0
                    lista_puntos = []

                #print 'click',pygame.mouse.get_pos()
                #print 'click',event.post
