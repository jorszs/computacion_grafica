import pygame
import time
import random
#definicion de variables

verde=[255,0,0]
azul = [0,0,100]
ALTO=600
ANCHO=600
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprite/nave.png")#pygame.Surface([30,30])
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 200
        self.vel_x = 0
        self.vel_y = 0
        self.salud = 5
    def update(self):
        self.rect.x += self.vel_x
        if self.rect.y >= 75:
            self.rect.y += self.vel_y

        else:

            self.rect.y = 75
            self.vel_y = 0
        if self.rect.y > (ALTO - self.rect.height):
            self.rect.y = ALTO - self.rect.height
class Enemigo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([225,0,0])
        self.rect = self.image.get_rect()
        self.vel_x = -5
        self.rect.x = 2*ANCHO
        self.rect.y = 200
        self.espera = random.randrange(50)
        self.disparar = False
        self.temp = random.randrange(100)

    def update(self):
        if self.temp > 0:
            self.temp -= 1
        else:
            self.disparar = True
        if self.espera > 0:
            self.espera -= 1
        else:
            self.rect.x += self.vel_x
class Bala (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,10])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.vel_x = 10

    def update(self):
        self.rect.x += self.vel_x

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
# grupos
    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balas_e = pygame.sprite.Group()
#objetos
    jugador = Jugador()
    jugadores.add(jugador)
    todos.add(jugador)



    num_enemigos = 10
    for i in range(num_enemigos):
        e = Enemigo()
        e.rect.x = random.randrange(ANCHO, ANCHO + 500)#e.rect.width)
        e.rect.y = random.randrange(ALTO - e.rect.height)#e.rect.height)
        enemigos.add(e)
        todos.add(e)
        fuente = pygame.font.Font(None, 32)
    reloj = pygame.time.Clock()
    ptos = 0


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



        #logica del juego
        #analizar coliciones
        ls_col = pygame.sprite.spritecollide(jugador, enemigos, True)

        for e in ls_col:
            ptos+=1
            print 'puntos: ', ptos

        eliminados = 0
        for b in balas_e:
            if b.rect.x < 0:
                b.remove()

            ls_colj = pygame.sprite.spritecollide(b, jugadores, False)
            if jugador in ls_colj:
                balas_e.remove(b)
                todos.remove(b)
                jugador.salud -= 1
                print 'salud', jugador.salud
#control de objetos
        for e in enemigos:
            if e.disparar:
                e.temp = random.randrange(100)
                e.disparar=False
                b = Bala()
                b.vel_x = -10
                b.rect.x = e.rect.x
                b.rect.y = e.rect.y
                b.image.fill(azul)
                balas_e.add(b)
                todos.add(b)

            if e.rect.x < 0:
                enemigos.remove(e)
                todos.remove(e)
                eliminados+=1
        for b in balas:
            ls_colb = pygame.sprite.spritecollide(b,enemigos,True)
            for e in ls_colb:
                enemigos.remove(e)
                todos.remove(e)
                balas.remove(e)
                eliminados +=1
        for i in range(eliminados):
            e = Enemigo()
            e.rect.x = random.randrange(ANCHO, ANCHO + 500)#e.rect.width)
            e.rect.y = random.randrange(75,ALTO - e.rect.height)#e.rect.height)
            enemigos.add(e)
            todos.add(e)

        for b in balas:
            if b.rect.x > ANCHO:
                balas.remove(b)
                todos.remove(b)

        #refresco de pantalla

        todos.update()
        pantalla.fill([0,0,0])
        texto = fuente.render("salud ", False, [255,155,155])
        txt_valor = fuente.render(str(jugador.salud),False,[255,155,155])
        pantalla.blit(texto, [50,10])
        pantalla.blit(txt_valor, [140, 10])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
