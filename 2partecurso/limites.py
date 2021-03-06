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
#grupos
    jugadores = pygame.sprite.Group()
    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    jugador = Jugador()
    jugadores.add(jugador)
    todos.add(jugador)

    enemigo = Enemigo(30,30,[ANCHO-300,ALTO-100])
    #enemigo.rect.x = random.randrange(ANCHO)
    #enemigo.rect.y = random.randrange(ALTO)
    todos.add(enemigo)
    enemigos.add(enemigo)

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
                  enemigo.vel_y = 5
                  '''b = Bala()
                  b.rect.x = jugador.rect.x
                  b.rect.y = jugador.rect.y
                  todos.add(b)
                  balas.add(b)'''
          if event.type == pygame.KEYUP:
              jugador.vel_y = 0
              jugador.vel_x = 0


      #logica del programa
      ls_col = pygame.sprite.spritecollide(jugador, muros, False)
      print ls_col
      ls_col_e = pygame.sprite.spritecollide(enemigo, muros, False)
      for m in ls_col_e:
          if (enemigo.vel_y > 0) and (enemigo.rect.bottom >= m.rect.top):
              enemigo.vel_y = 0
              enemigo.vel_x = -5

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

      '''for m in ls_col_e:
          if (enemigo.vel_y > 0) and (enemigo.rect.bottom >= m.rect.top):
              enemigo.vel_y = 0
              #enemigo.rect.bottom = m.rect.top
              enemigo.rect.y =ALTO-5
              enemigo.vel_x = -5

              #enemigo.vel_x = -5
              #enemigo.rect.bottom = m.rect.top
          if (enemigo.vel_x > 0) and (enemigo.rect.right >= m.rect.left):
              enemigo.vel_x = 0
              enemigo.rect.right = m.rect.left
              enemigo.vel_y = 5
              #enemigo.rect.right = m.rect.left
          if (enemigo.vel_x < 0) and (enemigo.rect.left <= m.rect.right):
              enemigo.vel_x = 0
              enemigo.rect.left = m.rect.right
              enemigo.vel_y = -5
              #enemigo.rect.left = m.rect.right
              #enemigo.vel_y = -5

              #enemigo.rect.left = m.rect.right
          if (enemigo.vel_y < 0) and (enemigo.rect.top <= m.rect.bottom):
              enemigo.vel_y = 0
              enemigo.rect.top = m.rect.bottom
              enemigo.vel_x = 5
              #enemigo.rect.top = m.rect.bottom'''


      #refresco de pantalla
      todos.update()
      pantalla.fill(Negro)
      todos.draw(pantalla)
      pygame.display.flip()
      reloj.tick(50)
