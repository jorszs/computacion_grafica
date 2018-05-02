import pygame
from fractions import Fraction
import math

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

def escalar (punto,num):
    '''punto[0]=punto[0]*(num)
    punto[1]=punto[1]*(num)
    return punto'''
    p=punto[0]*(num)
    o=punto[1]*(num)
    punto[0]=p;punto[1]=o
    return punto
def tras_aorigen(punto,pf):#transformar la figura al origen
    xp=punto[0]-pf[0]#xprima
    yp=punto[1]-pf[1]#yprima
    return [xp,yp]

def tras_dsdorigen(punto,pf):#transladar la figura desde al origen a la normalidad
    xp=punto[0]+pf[0]#xprima
    yp=punto[1]+pf[1]#yprima
    return [xp,yp]

def dibujar_p(lista,num):
    pf=lista[0]
    for punto in lista:
        #p=cart(centro,punto)
        p=tras_aorigen(punto,pf)
        p1=escalar(punto,num)
        p2=transformacion1(centro,p1)
        p3=tras_dsdorigen(p2,pf)
        lis.append(p3)
    return lis

def dibujar_origen(lista,num):
    pf=lista[0]
    print pf
    for punto in lista:
        #p=cart(centro,punto)
        p1=tras_aorigen(punto,pf)
        p2=escalar(p1,num)
        p3=tras_dsdorigen(p2,pf)
        p4=transformacion1(centro,p3)

        lis.append(p4)
        print pf
    return lis

def dibujar_rot(lista,num):
    pf=lista[0]
    print pf
    for punto in lista:
        #p=cart(centro,punto)
        p1=tras_aorigen(punto,pf)
        #p2=escalar(p1,num)
        p2=rotar(p1,num)
        p3=tras_dsdorigen(p2,pf)
        p4=transformacion1(centro,p3)

        lis.append(p4)
        print pf
    return lis
    #pygame.draw.polygon(pantalla,[0,155,200],lista,1)
#-----------------
if __name__ == '__main__':
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    centro=[ANCHO/2,ALTO/2]
    #ls=[[10,20],[40,20],[40,30]]
    #lis=[]

    #Ejes(pantalla,centro)
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
                    ls_p=dibujar_p(lista_clicks,2)
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    #print lista_clicks
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    lis=[]
                    ls_p=dibujar_p(lista_clicks,0.5)
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    lis=[]
                    laux=[]
                    laux=dibujar_origen(lista_clicks,2)
                    pygame.draw.polygon(pantalla,[25,200,100],laux,1)
                    pygame.display.flip()

                if event.key == pygame.K_LEFT:
                    lis=[]
                    laux=dibujar_rot(lista_clicks,90)
                    pygame.draw.polygon(pantalla,[25,200,100],laux,1)
                    pygame.display.flip()


        if cont == 4:
            listau=[]
            for v in lista_clicks:
                pn=transformacion1(centro,v)
                listau.append(pn)
            pygame.draw.polygon(pantalla,[2,154,200],listau,1)
            pygame.display.flip()
            cont=0
            lista_clicks
