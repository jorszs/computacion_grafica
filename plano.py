import pygame

def transformacion(a,b,x,y):
    x = a + x
    y = b - y
    return (x,y)

def transformacion1(centro,pto):
    pto[0] = centro[0] + pto[0]
    pto[1] = centro[1] - pto[1]
    return pto


if __name__ == '__main__':
    pygame.init()
    print 'probando...'
    lista = []
    pantalla = pygame.display.set_mode([600,400])
    pygame.draw.line(pantalla,[255,0,0],[200,0],[200,400])
    pygame.draw.line(pantalla,[255,0,0],[0,300],[600,300])
    pygame.draw.line(pantalla,[255,0,0],transformacion(200,300,-150,50),transformacion(200,300,0,0))
    #pygame.draw.line(pantalla,[255,0,0],transformacion(200,300,200,100),transformacion(200,300,0,0))
    pygame.draw.line(pantalla,[255,0,0],transformacion1([200,300],[200,100]),transformacion1([200,300],[0,0]))
    #dibuijar punto
    centro=[200,300]
    x = -200
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        y=int(100 + (3*x))
        if x <= 400:
            x+=1
        pygame.draw.circle(pantalla,[0,255,0],transformacion1(centro,[x,y]),1)
        pygame.display.flip()

    pygame.display.flip()
    con = 0

    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print 'click'
                con+=1
                if con ==1:
                    pos1=event.pos
                if con==2:
                    pos2=event.pos
                    pygame.draw.line(pantalla,[255,0,0],pos1,pos2)
                    pygame.display.flip()
                    con = 0

                print 'click',pygame.mouse.get_pos()
                #print 'click',event.post
