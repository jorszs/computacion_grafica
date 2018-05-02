import pygame
import random
import configparser

Alto=600;Ancho=600;Negro=[0,0,0]

def Recortar(nf,nc,archivo):
    imagen=pygame.image.load(archivo)
    info=imagen.get_rect()
    #informacion de ancho de imagen y alto de imagen
    an_img=info[2]
    al_img=info[3]
    #lo que divide son el numero de cortes horizontales
    an_corte=int(an_img/nc)
    #lo que divide son el numero de cortes verticales
    al_corte=int(al_img/nf)
    m=[]
    for y in range(nf):
        fila=[]
        for x in range(nc):
            #se crea una seubsurface con el corte de la imagen
            cuadro = imagen.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
            cuadro = pygame.transform.scale(cuadro,(60,60))
            fila.append(cuadro)
        m.append(fila)
    return m

if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])

    interprete=configparser.ConfigParser();
    interprete.read('mapa.map')
    archivo=interprete.get('nivel','origen'); # archivo guarda el nombre de la imagen
    al=int(interprete.get('nivel','al')) #con get obtengo la cadena de mapa.map para [nivel] donde al= 'valor' pero debo convertirlo a int para pasarlo a la variable al
    an=int(interprete.get('nivel','an'))
    m=Recortar(al,an,archivo)
    pantalla.blit(m[0][0],[0,0])

    infomapa=interprete.get('nivel','mapa')
    print (infomapa, type(infomapa))
    lt=infomapa.split('\n')

    print lt
    print lt[0]

    for e in lt[0]:
        print e, interprete.get(e,'nom')
        px=int(interprete.get(e,'x'))
        py=int(interprete.get(e,'y'))
        pantalla.blit(m[py][px],[0,0])

    print lt, type(lt)

    pygame.display.flip()
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              fin=True
