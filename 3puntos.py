import pygame

Ancho=600
Alto=400
Rojo= [255,0,0]
lista=[]
centro=[300,300]
Azul=[0,0,255]
Negro=[0,0,0]
a = 0
def ACart(c,p):
    x=p[0]-c[0]
    y=c[1]-p[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])


    pygame.display.flip()
    fin=False
    reloj=pygame.time.Clock()
    x=0
    var=1
    punto=[x,100]
    psp=[700,0]
    lista=[]
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                p = list(event.pos)
                lista.append(p)
                a+=1

        if a == 3:
            print len(lista)
            pantalla.fill([0,0,0])
            for v in lista:
                v[1]+=1
                pygame.draw.circle(pantalla,Azul,v,5)



        pygame.display.flip()
        reloj.tick(60)
