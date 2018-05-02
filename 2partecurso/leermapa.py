import pygame
import random
import ConfigParser
Alto=480
Ancho=640
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]
def Recortar(nf,nc,archivo):
    image=pygame.image.load(archivo)
    info=image.get_rect()
    an_img=info[2]
    al_img=info[3]
    an_corte=int(an_img/nc)
    al_corte=int(al_img/nf)
    m=[]
    for y in range(nf):
        fila=[]
        for x in range(nc):
            cuadro = image.subsurface(x*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m


if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    archivo = interprete.get('nivel','origen')
    al=int(interprete.get('nivel','al'))
    an=int(interprete.get('nivel','an'))
    m = Recortar(al,an,archivo)

    infomapa=interprete.get('nivel','mapa')
    print infomapa, type(infomapa)


    reloj=pygame.Clock()
    fin=False

    while not fin:
      #Gestion de eventos
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              fin=True

      #Refresco
      todos.update()
      pantalla.fill(negro)
      todos.draw(pantalla)
      #pantalla.blit(m[accion][i],[ps_x,ps_y])
      pygame.display.flip()
      reloj.tick(20)
