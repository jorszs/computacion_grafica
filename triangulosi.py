import pygame
from fractions import Fraction

#funciones--------

def transformacion1(centro,pto):
    x = centro[0] + pto[0]
    y = centro[1] - pto[1]
    return [x,y]

def cart(cen,pto_pantalla):
    xp=pto_pantalla[0]-cen[0]
    yp=cen[1]-pto_pantalla[1]
    return [xp,yp]

def rotar (punto,num):
    punto[0]=punto[0]*(num)
    punto[1]=punto[1]*(num)
    return punto

def dibujar_p(lista,num):
    for punto in lista:
        p1=rotar(punto,num)
        p2=transformacion1(centro,p1)
        lis.append(p2)
    return lis
    #pygame.draw.polygon(pantalla,[0,155,200],lista,1)
#-----------------
if __name__ == '__main__':
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    centro=[150,300]
    ls=[[10,20],[40,20],[40,30]]
    #lis=[]

    #Ejes(pantalla,centro)
    ls_p=[]
    #dibujar el primer triangulo

    for p in ls:
        np = transformacion1(centro,p)
        ls_p.append(np)
    pygame.draw.polygon(pantalla,[0,255,0],ls_p,1)
    #dibujar el plano cartesiano
    pygame.draw.line(pantalla,[0,255,255],[150,0],[150,ALTO])
    pygame.draw.line(pantalla,[0,255,255],[0,300],[ANCHO,300])
    pygame.display.flip()
    ls2=[[10,20],[40,20],[40,30]]

    print ls2

    cont = 0
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    lis=[]

                    ls_p=dibujar_p(ls2,2)
                    print ls2
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    lis=[]
                    ls_p=dibujar_p(ls2,-2)
                    print ls2
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    pygame.display.flip()
