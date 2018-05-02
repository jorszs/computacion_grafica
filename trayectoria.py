import pygame

Ancho=610
Alto=600
Rojo= [255,0,0]
lista=[]
centro=[300,300]
Azul=[0,0,255]
Negro=[0,0,0]
E=0
def ACart(c,p):
    x=p[0]-c[0]
    y=c[1]-p[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    #Dibujo del plano cartesiano
    pygame.draw.line(pantalla,Rojo,[centro[0],0],[centro[0],Alto])
    pygame.draw.line(pantalla,Rojo,[0,centro[1]],[Ancho,centro[1]])

    pygame.display.flip()
    fin=False
    reloj=pygame.time.Clock()
    v1=[280,10]
    v2=[320,10]
    limite = 300
    lista.append(v1)
    lista.append(v2)

    x=0
    y=0
    var=1
    punto=[x,y]
    psp=[700,0]
    while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
            for v in lista:
                if v[1] < limite:
                    v[1]+=1
                    #pygame.draw.circule(pantalla,Rojo,v,4)
                else:
                    if v[0] <= 300:
                        v[0]-=1
                    else:
                        v[0]+=2
                pygame.draw.circle(pantalla,Rojo,v,4)

                pygame.display.flip()
                reloj.tick(100)
