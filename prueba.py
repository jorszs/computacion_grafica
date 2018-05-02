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
    centro=[200,300]
    ls=[[20,20],[70,20],[70,50]]
    #Ejes(pantalla,centro)
    pygame.draw.line(pantalla,[255,0,0],[200,0],[200,400])
    pygame.draw.line(pantalla,[255,0,0],[0,300],[600,300])
    fin=False
    pygame.display.flip()
    cont = 0
    lis_putos=[]
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                a = pygame.event.get()
                lis_putos.append(a)

        if cont == 3:
            pygame.draw.polygon(pantalla,[0,255,0],lis_putos,1)
