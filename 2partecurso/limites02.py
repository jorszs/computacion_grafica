import pygame
import time
import random
#definicion de variables

verde=[255,0,0]
azul = [0,0,100]
ALTO=600
ANCHO=600
blanco = [20,10,30]
Negro=[0,0,0]


class Muro(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill(blanco)
        self.rect = self.image.get_rect()

class Enemigo (pygame.sprite.Sprite):
    def __init__(self,an,al,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill([15,200,10])
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    #GRUPOS
    enemigos = pygame.sprite.Group()
    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    #ENTES
    enemigo = Enemigo(30,30,[ANCHO-300,ALTO-100])
    enemigos.add(enemigo)
    todos.add(enemigo)

    m = Muro(70,100)
    m.rect.x = 300
    m.rect.y = 250
    todos.add(m)
    muros.add(m)

    m2 = Muro(100,30)
    m2.rect.x = 100
    m2.rect.y = 250
    todos.add(m2)
    muros.add(m2)

    m3 = Muro(100,30)
    m3.rect.x = 400
    m3.rect.y = 350
    todos.add(m3)
    muros.add(m3)
    #limites de pantalla
    limite_i = Muro(20,ALTO)
    limite_i.rect.x = 0
    limite_i.rect.y = 0
    todos.add(limite_i)
    muros.add(limite_i)

    limite_d = Muro(20,ALTO)
    limite_d.rect.x = ANCHO-20
    limite_d.rect.y = 0
    todos.add(limite_d)
    muros.add(limite_d)

    limite_s = Muro(ANCHO,20)
    limite_s.rect.x = 20
    limite_s.rect.y = 0
    todos.add(limite_s)
    muros.add(limite_s)

    limite_in = Muro(ANCHO,20)
    limite_in.rect.x = 0
    limite_in.rect.y = ALTO-20
    todos.add(limite_in)
    muros.add(limite_in)

    reloj = pygame.time.Clock()
    fin = False
    while not fin:
      #gestion de eventos
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              fin = True

          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                  enemigo.vel_x = -5

      #logica del programa
      ls_col = pygame.sprite.spritecollide(enemigo,muros,False)
      '''for m in ls_col:
          if (enemigo.vel_y > 0) and (enemigo.rect.bottom >= m.rect.top):
              enemigo.vel_y = 0
              enemigo.vel_x = -5
          elif (enemigo.vel_y < 0) and (enemigo.rect.top <= m.rect.bottom):
              enemigo.vel_y = 0
              #enemigo.rect.top = m.rect.bottom
              enemigo.vel_x = 5
              #enemigo.rect.top = m.rect.bottom

          elif (enemigo.vel_x < 0) and (enemigo.rect.left <= m.rect.right):
              enemigo.vel_x = 0
              #enemigo.rect.left = m.rect.right
              enemigo.vel_y = -5
          else:
              if (enemigo.vel_x > 0) and (enemigo.rect.right >= m.rect.left):
                  enemigo.vel_x = 0
                  #enemigo.rect.right = m.rect.left
                  enemigo.vel_y = 5'''
      for m in ls_col:
          if (enemigo.vel_y > 0) and (enemigo.rect.bottom >= m.rect.top):
              enemigo.rect.bottom = m.rect.top-1
              enemigo.vel_y = 0
              enemigo.vel_x = -5

          if (enemigo.vel_y < 0) and (enemigo.rect.top <= m.rect.bottom) and (enemigo.rect.left <= m.rect.right):
              enemigo.rect.top = m.rect.bottom+1
              enemigo.vel_y = 0
              #enemigo.rect.x = 21
              #enemigo.rect.top = m.rect.bottom
              enemigo.vel_x = 5
              #enemigo.rect.top = m.rect.bottom

          if (enemigo.vel_x < 0) and (enemigo.rect.left <= m.rect.right):
              enemigo.rect.left = m.rect.right+10
              enemigo.vel_x = 0
              enemigo.vel_y = -5
          if (enemigo.vel_x > 0) and (enemigo.rect.right >= m.rect.left):
              enemigo.rect.right = m.rect.left-1
              enemigo.vel_x = 0
              #enemigo.rect.right = m.rect.left
              enemigo.vel_y = 5
      #refresco de pantalla
      todos.update()
      pantalla.fill(Negro)
      todos.draw(pantalla)
      pygame.display.flip()
      reloj.tick(50)
