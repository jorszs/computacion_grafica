import pygame
from fractions import Fraction
import math

"""descripcion del problema:
    1.dibujar un cuadrilatero, siendo cada vertice(punto) la captura
    de la posicion del mouse al hacer click
    2.escalar el triangulo en 0.4, tomando punto fijo la
    primer posicion de clcik capturada


"""


#funciones--------
#transforma el punto cartesiano a pantalla
def transformacion1(centro,pto):
    x = centro[0] + pto[0]
    y = centro[1] - pto[1]
    return [x,y]
#transforma el punto pantalla a punto cartesiano
def cart(cen,pto_pantalla):
    xp=pto_pantalla[0]-cen[0]
    yp=cen[1]-pto_pantalla[1]
    return [xp,yp]
#escala el punto en num
def escalar (punto,num):
    p=punto[0]*(num)
    o=punto[1]*(num)
    punto[0]=p;punto[1]=o
    return punto
#traslada el punto al origen del plano carteniano
#pf es el punto fijo
def tras_aorigen(punto,pf):#sirve para transformar la figura al origen
    xp=punto[0]-pf[0]#xprima
    yp=punto[1]-pf[1]#yprima
    return [xp,yp]
#trasforma la figura desde el origen a donde fue dibujada
def tras_dsdorigen(punto,pf):
    xp=punto[0]+pf[0]#xprima
    yp=punto[1]+pf[1]#yprima
    return [xp,yp]


#dibuja la figura escalada en "num" recibiendo la lista de puntos
def dibujar_ptofijo(lista,num):
    pf=lista[0]#hace que el punto fijo sea el primero de la lista,(el click que capturo )
    print pf
    for punto in lista:
        p1=tras_aorigen(punto,pf)
        p2=escalar(p1,num)
        p3=tras_dsdorigen(p2,pf)
        p4=transformacion1(centro,p3)

        lis.append(p4)
        print pf
    return lis



#-----------------
if __name__ == '__main__':
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    centro=[ANCHO/2,ALTO/2]

    ls_p=[]


    #dibujar el plano cartesiano
    pygame.draw.line(pantalla,[0,255,255],[ANCHO/2,0],[ANCHO/2,ALTO])
    pygame.draw.line(pantalla,[0,255,255],[0,ALTO/2],[ANCHO,ALTO/2])
    pygame.display.flip()

    lista_clicks=[]

    cont = 0
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            #esta parte captura los clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                cont+=1
                #print cont
                lista_clicks.append(cart(centro,event.pos))#*

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    lis=[]
                    laux=[]
                    laux=dibujar_ptofijo(lista_clicks,0.4)
                    pygame.draw.polygon(pantalla,[25,200,100],laux,1)
                    pygame.display.flip()



        if cont == 4:#me garantiza que a los 4 clicks me va a dibujar el cuadrilatero
            listau=[]
            for v in lista_clicks:
                pn=transformacion1(centro,v)
                listau.append(pn)
            pygame.draw.polygon(pantalla,[2,154,200],listau,1)
            pygame.display.flip()
            cont=0
            lista_clicks
