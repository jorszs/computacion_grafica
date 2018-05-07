import pygame
import random

Alto=480
Ancho=640
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]

class cuadro (pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.rect = self.image.get_rect()
        self.image.fill(Blanco)
        self.rect.x = 300
        self.rect.y = 200

if __name__ == '__main__':
    #Definicion de variables

    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    todos = pygame.sprite.Group()
    c = cuadro(50,50)
    todos.add(c)
    reloj=pygame.time.Clock()
    fin=False
    while not fin:

      pos = pygame.mouse.get_pos()
#Gestion de eventos
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              fin=True
      '''if c.rect.collidepoint(pos) == 1:
          c.rect.center = pos
          print 'contacto''''
          if event.type == pygame.MOUSEBUTTONDOWN:
              if c.rect.collidepoint(pos) == 1:
                  c.rect.center = pos
      pantalla.fill(Negro)
      todos.draw(pantalla)
      pygame.display.flip()
      reloj.tick(50)
