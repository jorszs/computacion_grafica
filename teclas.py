import pygame
import math
#Dibuja triangulo y lo escala con el teclado
ANCHO=600
ALTO=480

def dibujarPlano(o, pantalla):
    pygame.draw.line(pantalla, [0, 255, 0], [o[0], 0], [o[0], 480] )
    pygame.draw.line(pantalla, [0, 255, 0], [0, o[1]], [640, o[1]] )

def calcularPosPantalla(o, p):
    return o[0]+p[0], o[1]-p[1]

def dibujarTriangulo(a, b, c, plano):
    '''
    pygame.draw.line(plano, [0, 255, 0], [a[0], a[1]], [b[0], b[1]] )
    pygame.draw.line(plano, [0, 255, 0], [b[0], b[1]], [c[0], c[1]] )
    pygame.draw.line(plano, [0, 255, 0], [c[0], c[1]], [a[0], a[1]] )
    '''
    pygame.draw.polygon(plano, [0, 255, 0], [a,b,c])
    pygame.display.flip()
    return a, b, c

def mostrarPos():
    pos=pygame.mouse.get_pos()
    return pos

def escalarPunto (a, factor):
    return a[0]*factor, a[1]*factor

def rotacionHoraria(a):
    #xcos-ysen, xsen+ycos
    return abs(int(a[0]*math.cos(math.pi/2) - a[1]*math.sin(math.pi/2))), abs(int(a[0]*math.sin(math.pi/2) + a[1]*math.cos(math.pi/2)))

def rotacionAntiHoraria(a):
    #xcos-ysen, xsen+ycos
    return abs(int(a[0]*math.cos(math.pi/2) - a[1]*math.sin(math.pi/2))), abs(int(a[0]*math.sin(math.pi/2) + a[1]*math.cos(math.pi/2)))



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    #o=[ANCHO/2, ALTO/2]
    #dibujarPlano(o, pantalla)
    pygame.display.flip()
    print 'Funciona'
    cont=0
    lista=[]
    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                lista.append(mostrarPos())

            if event.type == pygame.KEYDOWN:

                if event.key==pygame.K_RIGHT:
                    pantalla.fill([0, 0, 0])
                    puntos=lista
                    '''
                    print 'Puntos iniciales:'
                    print puntos
                    '''
                    puntos[0]=rotacionHoraria(puntos[0])
                    puntos[1]=rotacionHoraria(puntos[1])
                    puntos[2]=rotacionHoraria(puntos[2])
                    ''''
                    print 'Puntos finales:'
                    print puntos
                    '''
                    dibujarTriangulo(puntos[0], puntos[1], puntos[2], pantalla)


                if event.key==pygame.K_LEFT:
                    pantalla.fill([0, 0, 0])
                    puntos=lista
                    '''
                    print 'Puntos iniciales:'
                    print puntos
                    '''
                    puntos[0]=rotacionAntiHoraria(puntos[0])
                    puntos[1]=rotacionAntiHoraria(puntos[1])
                    puntos[2]=rotacionAntiHoraria(puntos[2])
                    '''
                    print 'Puntos finales:'
                    print puntos
                    '''
                    dibujarTriangulo(puntos[0], puntos[1], puntos[2], pantalla)

            if cont==3:
                dibujarTriangulo(lista[0], lista[1], lista[2], pantalla)
                cont=0
                #lista=[]
