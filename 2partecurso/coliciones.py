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

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 150
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Muro(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill(blanco)
        self.rect = self.image.get_rect()
if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
#grupos
    jugadores = pygame.sprite.Group()
    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    jugador = Jugador()
    jugadores.add(jugador)
    todos.add(jugador)

    m = Muro(70,100)
    m.rect.x = 300
    m.rect.y = 250
    todos.add(m)
    muros.add(m)


    reloj = pygame.time.Clock()
    fin = False
    while not fin:

      #gestion de eventos
      for event in pygame.event.get():

          if event.type == pygame.QUIT:
              fin =True

          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RIGHT:
                  jugador.vel_x = 5
                  jugador.vel_y = 0
              if event.key == pygame.K_LEFT:
                  jugador.vel_x = -5
                  jugador.vel_y = 0
              if event.key == pygame.K_DOWN:
                  jugador.vel_y = 5
                  jugador.vel_x = 0
              if event.key == pygame.K_UP:
                  jugador.vel_y = -5
                  jugador.vel_x = 0
              if event.key == pygame.K_SPACE:
                  b = Bala()
                  b.rect.x = jugador.rect.x
                  b.rect.y = jugador.rect.y
                  todos.add(b)
                  balas.add(b)
              if event.key == pygame.KEYUP:
                  jugador.vel_y = 0



      #logica del programa
      ls_col = pygame.sprite.spritecollide(jugador, muros, False)
      for m in ls_col:

          if (jugador.vel_y > 0) and (jugador.rect.bottom >= m.rect.top):
              jugador.vel_y = 0
              jugador.rect.bottom = m.rect.top
          if (jugador.vel_x > 0) and (jugador.rect.right >= m.rect.left):
              jugador.vel_x = 0
              jugador.rect.right = m.rect.left
          if (jugador.vel_x < 0) and (jugador.rect.left <= m.rect.right):
              jugador.vel_x = 0
              jugador.rect.left = m.rect.right
          if (jugador.vel_y < 0) and (jugador.rect.top <= m.rect.bottom):
              jugador.vel_y = 0
              jugador.rect.top = m.rect.bottom
      #refresco de pantalla
      todos.update()
      pantalla.fill(Negro)
      todos.draw(pantalla)
      pygame.display.flip()
      reloj.tick(50)
