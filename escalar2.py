import pygame #al iniciar programa dibujar triangulo dando tres clics
ancho=800; alto=600  #dimensiones
verde = [0,255,0] ; rojo = [255,0,0] ;negro = [0,0,0];otrocol=[40,30,200]
reloj = pygame.time.Clock()  #reloj para manejar tiempo
centro = [int(ancho/2),int(alto/2)]

def escalar(pto,pEs): # recibe los puntos en una lista ls, y el punto que tiene los escalamientos pEs
    return [pto[0]*pEs[0],pto[1]*pEs[1]]

def trans_pantalla(cen,pto_cartesiano):#transformacion lineal recibe c Centro y devuelve el punto en pantalla
    x = int(cen[0] + pto_cartesiano[0])
    y = int(cen[1] - pto_cartesiano[1])
    return [x,y]

def cart(cen,pto_pantalla):
    xp=pto_pantalla[0]-cen[0]
    yp=cen[1]-pto_pantalla[1]
    print (xp,yp)
    return [xp,yp]

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    lsptos=[] ;
    fin=False
    cont=0


    while not fin:
        reloj.tick(40)
        pygame.draw.line(pantalla,rojo,[ancho/2,0],[ancho/2,alto])
        pygame.draw.line(pantalla,rojo,[0,alto/2],[ancho,alto/2])
        pygame.draw.circle(pantalla,verde,centro,1)
        if len(lsptos) >= 3:
            pygame.draw.polygon(pantalla,otrocol,lsptos,2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont >= 3:
                    lsptos = []
                    cont = 0
                if cont < 3:
                    lsptos.append(list(event.pos))
                    cont +=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    for p in lsptos:
                        f = trans_pantalla(centro,escalar(cart(centro,p),[2,2]))
                        lsptos[lsptos.index(p)] = f
                    otrocol = [100,87,120]
                    print (lsptos)

                if event.key == pygame.K_DOWN:
                    if cont == 3:
                        for p in lsptos:
                            f = trans_pantalla(centro,escalar(cart(centro,p),[-0.5,-0.5]))
                            lsptos[lsptos.index(p)] = f
                        otrocol = [100,87,120]
                        print (lsptos)
