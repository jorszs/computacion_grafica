import pygame
import math

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

def rotar(punto,angulo):
    angulo = math.radians(angulo)
    #print angulo
    a=int(math.cos(angulo))
    b=int(math.sin(angulo))
    p=punto[0]*a-punto[1]*b#xr = x rotado
    q=punto[0]*b+punto[1]*a
    #punto=[p,q]
    punto[0]=p;punto[1]=q
    #print punto
    #print [p,q]
    return punto

def dibujar_rot(lista,num):
    for punto in lista:
        #p=cart(centro,punto)
        p2=0
        p1=rotar(punto,num)
        #print p1
        p2=transformacion1(centro,p1)
        #print p2
        lis.append(p2)
    print lis
    return lis
#funcion rotar triangulo 90g



if __name__ == '__main__':
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    centro=[ANCHO/2,ALTO/2]
    ls_p=[]
    #dibujar el primer triangulo

    #for p in ls:
    #    np = transformacion1(centro,p)
    #    ls_p.append(np)
    #pygame.draw.polygon(pantalla,[0,255,0],ls_p,1)
    #dibujar el plano cartesiano
    pygame.draw.line(pantalla,[0,255,255],[ANCHO/2,0],[ANCHO/2,ALTO])
    pygame.draw.line(pantalla,[0,255,255],[0,ALTO/2],[ANCHO,ALTO/2])
    pygame.display.flip()
    #ls2=[[10,20],[40,20],[40,30]]
    lista_clicks=[]
    #lista_clicks=[[10,10],[30,10],[30,20]]
    #pygame.draw.polygon(pantalla,[255,255,0],lista_clicks,1)
    #pygame.display.flip()

    #print ls2

    cont = 0
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True

            if event.type == pygame.MOUSEBUTTONDOWN:

                cont+=1
                print cont
                #lista_clicks.append([event.pos[0],event.pos[1]])#convierto el punto posicion a cartesiano
                lista_clicks.append(cart(centro,event.pos))#*
                #print lista_clicks
                #while cont <3:
                #    print "waba loba docdoc"
                #    lista_clicks.append(cart(centro,event.pos))#convierto el punto posicion a cartesiano

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    lis=[]
                    #print lista_clicks
                    ls_p=dibujar_rot(lista_clicks,90)
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    #print lista_clicks
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    lis=[]
                    ls_p=dibujar_rot(lista_clicks,180)
                    #print ls_p
                    #print "----------"
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    print rotar(lista_clicks[0],90)
                    print rotar(lista_clicks[1],90)
                    print rotar(lista_clicks[2],90)
                    print int(math.cos(math.radians(270)))

        if cont == 3:
            listau=[]
            for v in lista_clicks:
                pn=transformacion1(centro,v)
                listau.append(pn)
            pygame.draw.polygon(pantalla,[2,154,200],listau,1)
            pygame.display.flip()
            cont=0
