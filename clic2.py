#clic
import pygame
alto = 480
ancho = 640
rojo = [255,0,0]

def convierte(c,p):
    x = p[0] - c[0]
    y = c[1] - p[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()                 #siempre debemos inicializar
    pantalla = pygame.display.set_mode([ancho,alto])
    centro =[350,250]
    pygame.draw.line(pantalla,rojo,[0,centro[1]],[ancho,centro[1]])
    pygame.draw.line(pantalla,rojo,[centro[0],0],[centro[0],alto])
    pygame.display.flip()
    x = 0
    y = 0
    punto =[x,100]
    reloj = pygame.time.Clock()
    fin = False
    cambia = True
    while not fin:
        if cambia:
            x+=1
            punto [0] = x
            print (x)
            pantalla.fill([0,0,0])
            pygame.draw.line(pantalla,rojo,[0,centro[1]],[ancho,centro[1]])
            pygame.draw.line(pantalla,rojo,[centro[0],0],[centro[0],alto])
            pygame.draw.circle(pantalla,rojo,punto,5,1)
            pygame.display.flip()
            reloj.tick(5)
        if not cambia:
            pun = event.pos
            y+=1
            punto [1] = y
            print (y)
            pantalla.fill([0,0,0])
            pygame.draw.line(pantalla,rojo,[0,centro[1]],[ancho,centro[1]])
            pygame.draw.line(pantalla,rojo,[centro[0],0],[centro[0],alto])
            pygame.draw.circle(pantalla,rojo,pun,5,1)
            pygame.display.flip()
            reloj.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                cambia= not(cambia)

                print ('clic',event.pos,convierte(centro, event.pos))
                pygame.draw.circle(pantalla,rojo,event.pos,5,1)
                pygame.display.flip()

            if event.type == pygame.QUIT:
                fin = True
