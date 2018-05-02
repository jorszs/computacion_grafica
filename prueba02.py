import pygame
import time
import random
verde=[0,0,225]
ALTO=600
ANCHO=600
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 200
        self.vel_x = 0
        self.vel_y = 0
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
class Enemigo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([225,0,0])
        self.rect = self.image.get_rect()
        self.vel_x = 5
        self.rect.x = 2*ANCHO
        self.rect.y = 200

    def update(self):
        self.rect.x += self.vel_x

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    jugador = Jugador()
    jugadores.add(jugadores)
    todos.add(jugador)



    num_enemigos = 10
    for i in range(num_enemigos):
        e = Enemigo()
        e.rect.x = random.randrange(ANCHO - e.rect.width)
        e.rect.y = random.randrange(ALTO - e.rect.height)
        enemigos.add(e)
        todos.add(e)

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
        #logica del juego
        #refresco de pantalla

        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
