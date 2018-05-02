import pygame

def transformacion(a,b,x,y):
    x = a + x
    y = b - y
    return (x,y)

def transformacion1(centro,pto):
    pto[0] = centro[0] + pto[0]
    pto[1] = centro[1] - pto[1]
    return pto

def Escala(p,s):
    xp=p[0]*s[0]
    yp=p[1]*s[1]
    return [xp,yp]


if __name__ == '__main__':
    pygame.init()

    pantalla = pygame.display.set_mode([600,400])
    centro=[150,350]
    ls=[[20,20],[70,20],[70,50]]
    #Ejes(pantalla,centro)
    pygame.draw.line(pantalla,[0,255,255],[150,0],[150,350])
    ls_p=[]
    for p in ls:
        np = transformacion1(centro,p)
        ls_p.append(np)
    pygame.draw.polygon(pantalla,[0,255,0],ls_p,1)

    ls_escala=[]

    for p in ls:
        np=Escala(p,(2,2))
        ls_escala.append(np)

    ls_p=[]
    for p in ls_escala:
        np=transformacion1(centro,p)
        ls_p.append(np)

    #pygame.draw.polygon(pantalla,[0,255,0],ls_p,1)
    pygame.display.flip()
    fin = False
    while not fin:
        for event in pygame.event.get():
            pass
