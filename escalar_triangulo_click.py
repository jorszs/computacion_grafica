import pygame
from fractions import Fraction
'''escalar triangulo
1.dibujar triangulo con clicks(tres clicks en la pantalla)
2.flecha hacia arriba para escalar el doble del triangulo
3.flecha hacia abajo para escalar en 0.5 el triangulo
'''
#funciones--------
#trasforma un punto de cartesiano a pantalla
def transformacion1(centro,pto):#pto es el punto cartesiano
    x = centro[0] + pto[0]
    y = centro[1] - pto[1]
    return [x,y]
#transforma el punto de pantalla a cartesiano
def cart(cen,pto_pantalla):
    xp=pto_pantalla[0]-cen[0]
    yp=cen[1]-pto_pantalla[1]
    return [xp,yp]
#escala el punto el numero "num", que le especifiquemos
def escalar (punto,num):#tener en cuenta: escala el punto cartesiano
    p=punto[0]*(num)
    o=punto[1]*(num)
    punto[0]=p;punto[1]=o
    return punto
#escala el triangulo, recbe la lista de vertices del triangulo
#y el numero "num" al que se va a escalar.
def escalar_triangulo(lista,num):
    for punto in lista:
        p1=escalar(punto,num)
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

            if event.type == pygame.MOUSEBUTTONDOWN:

                cont+=1
                print cont
                lista_clicks.append(cart(centro,event.pos))#captura la posicion del click y se tranforman a cartesiano

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    lis=[]
                    #print lista_clicks
                    ls_p=escalar_triangulo(lista_clicks,2)
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    #print lista_clicks
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    lis=[]
                    ls_p=escalar_triangulo(lista_clicks,0.5)
                    pygame.draw.polygon(pantalla,[2,154,200],ls_p,1)
                    pygame.display.flip()

        if cont == 3:#me garantiza que al capturar 3 clicks me va a dibujar la figura (triangulo)
            listau=[]
            for v in lista_clicks:
                pn=transformacion1(centro,v)
                listau.append(pn)
            pygame.draw.polygon(pantalla,[2,154,200],listau,1)
            pygame.display.flip()
            cont=0
