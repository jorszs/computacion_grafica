#Escalamiento punto fijo

import pygame
import math

ancho=600
alto=600
centro=[300,300]

def apantalla(c,p):
    x = c[0] + p[0]
    y = c[1] - p[1]
    return [x,y]

def acartesiana(c,p):
    x=p[0]-c[0]
    y=c[1]-p[1]
    return [x,y]

def escala(p,S):
    x = int(p[0]*S[0])
    y = int(p[1]*S[1])
    return [x,y]

def mov_00(p,f):
    x = p[0]-f[0]
    y = p[1]-f[1]
    return [x,y]

def mov_ori(p,f):
    x = p[0]+f[0]
    y = p[1]+f[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pygame.draw.line(pantalla,0xff2d00,[0,300],[600,300])
    pygame.draw.line(pantalla,0xff2d00,[300,0],[300,600])
    var=0
    lista=[]
    lista1=[[],[],[]]
    lista2=[]
    cambio=[1,1]
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ps1=list(event.pos)
                pygame.draw.circle(pantalla,0xff2d00,ps1,4)
                lista.append(ps1)
                lista2.append(acartesiana(centro,ps1))
                var+=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    cambio[0]=cambio[0]*0.5
                    cambio[1]=cambio[1]*0.5
                if event.key == pygame.K_UP:
                    cambio[0]=cambio[0]*1.5
                    cambio[1]=cambio[1]*1.5


        if var == 3:
            pantalla.fill([0,0,0])
            pygame.draw.polygon(pantalla,0xff2d00,lista,5)
            pygame.draw.line(pantalla,0xff2d00,[0,300],[600,300])
            pygame.draw.line(pantalla,0xff2d00,[300,0],[300,600])
            p1=mov_00(acartesiana(centro,lista[0]),lista2[0])
            p2=mov_00(acartesiana(centro,lista[1]),lista2[0])
            p3=mov_00(acartesiana(centro,lista[2]),lista2[0])
            lista1[0]=apantalla(centro,mov_ori(escala(p1,cambio),lista2[0]))
            lista1[1]=apantalla(centro,mov_ori(escala(p2,cambio),lista2[0]))
            lista1[2]=apantalla(centro,mov_ori(escala(p3,cambio),lista2[0]))

            pygame.draw.polygon(pantalla,[51,255,100],lista1,1)

        pygame.display.flip()
