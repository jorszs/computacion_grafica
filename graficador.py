#gr01

import pygame
#transformacion cartesiana a pantalla
def Operaciones(c1,c2,x1,y1):#transformacion lineal recibe c1,c2 Centro y devuelve el punto en pantalla
    x = int(c1 + x1)
    y = int(c2 - y1)
    return [x,y]

def CalcFuncion(x2):
    y2 = 5*x2+20
    pun=Operaciones(200,300,x2,y2)
    return pun

def Pintar():
    xs = -200
    while xs <= 400:
        pun = CalcFuncion(xs)
        pygame.draw.circle(pantalla,[255,0,0],pun,1)
        pygame.display.flip()
        xs += 0.5


if __name__ == '__main__':
    pygame.init()                 #siempre debemos inicializar
    pantalla = pygame.display.set_mode([600,400])
    fin=False
    con=0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if  event.type == pygame.MOUSEBUTTONDOWN:
                q = event.pos
                pygame.draw.line(pantalla,[255,0,0],[0,300],[600,300])
                pygame.draw.line(pantalla,[255,0,0],[200,0],[200,400])
                #pto = Operaciones(200,300,200,100)
                pygame.display.flip()
                Pintar()
