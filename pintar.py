#01
import pygame

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([600,500]); pantalla.fill([255,255,255])
    fin = False
    event = pygame.event.get()
    cont = 0
    x = (100,100)
    y = (0,0)
    pinta = True
    color1 = 40
    color2= 200
    color3 = 150
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION and pinta == True:
                    pygame.draw.circle(pantalla,[color1,color2,color3],event.pos,10)
                    pygame.display.flip()
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pinta = not(pinta)
                print ('clic')
                if color1 == 255 and color2 == 255 and color3 == 255:
                    color1 = 40
                    color2 = 200
                    color3 = 150
                if color1 == 40 and color2 == 200 and color3 == 150:
                    color1= 255
                    color2 = 255
                    color3 = 255
                if cont == 0:
                    x = event.pos
                    cont+=1
                if cont == 1:
                    y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                print ('\n\nlinea')
                pygame.draw.line(pantalla,[255,0,0],x,y)
                pygame.display.flip()
