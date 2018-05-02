import pygame

def transformacion1(centro,pto):
    pto[0] = centro[0] + pto[0]
    pto[1] = centro[1] - pto[1]
    return pto

#transformar puntos al plano cartesiano
def trans (lista):
#    ls_p=[]

    for p in lista:
        np = transformacion1(centro,p)
        ls_p.append(np)




#funcion de rotacion
def rotar (valor):
    for v in ls2:
         v[0]=v[0]*valor
         v[1]=v[1]*valor


#funcion main
if __name__ == '__main__':
    pygame.init()

    ALTO=800
    ANCHO=800
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    centro=[150,300]
    ls=[[10,20],[40,20],[40,30]]
    ls2=ls[:]
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


    cont = 0
    fin = False
    #capturar los diferentes tipos de eventos
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #print ls_p
                    #ls_q = rotar(ls,2)
                    #print ls_q
                    ls_p=[]
                    '''for p in ls_q:
                        np = transformacion1(centro,p)
                        ls_p.append(np)

                    print("probando")

                    pygame.draw.circle(pantalla,[255,0,0],ls_p[0],5)
                    pygame.draw.circle(pantalla,[255,0,0],ls_p[1],5)
                    pygame.draw.circle(pantalla,[255,0,0],ls_p[2],5)'''
                    print "lista normal";print ls2
                    rotar(2)
                    trans(ls_p)
                    pygame.draw.polygon(pantalla,[255,0,0],ls_p,1)
                    print "lista sin rotar ";print ls2;print " lista rotada "; print ls_p
                    pygame.display.flip()
                    #print ls_p
