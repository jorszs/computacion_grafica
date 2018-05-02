import pygame
import time
import random
#definicion de variables

verde=[255,0,0]
azul = [0,0,100]
ALTO=500
ANCHO=700
#accion = 0
def Recortar(nf,nc,archivo,limites):
    image=pygame.image.load(archivo)
    info=image.get_rect()
    an_img=info[2]
    al_img=info[3]
    an_corte=int(an_img/nc)
    al_corte=int(al_img/nf)
    m=[]
    for y in range(nf):
        fila=[]
        for x in range(limites[y]):
            cuadro = image.subsurface(x*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m

def matriz ():
    limites = [1]
    m=Recortar(1,1,'sprites/nave.png',limites)
    lista=[]
    lista.append(pygame.image.load('sprites/navederecha.png'))
    m.append(lista)
    lista=[]
    lista.append(pygame.image.load('sprites/naveizquierda.png'))
    m.append(lista)
    lista = []
    lista.append(pygame.image.load('sprites/nave2.png'))
    m.append(lista)
    return m

def matriz2 ():
    #limites = [1]
    #m=Recortar(1,1,'sprites/nave.png',limites)
    lista=[]
    m=[]
    lista.append(pygame.image.load('sprites/nave2.png'))
    m.append(lista)
    return m


class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.i = 0
        self.m = m
        self.accion = 0
        self.image = m[self.accion][0]#self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 200
        self.vel_x = 0
        self.vel_y = 0
        self.salud = 5
    def set_accion(self,accion):
        self.accion = accion
    def update(self):
        #actualiza velocidad
        #self.rect.x += self.vel_x
        #controla limites de pantalla
        if self.rect.y >= 75:
            self.rect.y += self.vel_y

        else:

            self.rect.y = 75
            self.vel_y = 0
        if self.rect.y > (ALTO - self.rect.height):
            self.rect.y = ALTO - self.rect.height
        if self.rect.x <= (ANCHO-130) and self.rect.x >= -60:
            self.rect.x += self.vel_x#self.rect.x = ANCHO - 40
        elif self.rect.x <= -60:
            self.rect.x = -60
            self.vel_x = 0

        elif self.rect.x >= ANCHO-130:
            self.rect.x = ANCHO-130
            self.vel_x = 0
        #actualiza el sprite
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i = 0

        self.image = self.m[self.accion][0]
#clase enemigo
class Enemigo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([225,0,0])
        self.rect = self.image.get_rect()
        self.vel_x = -5
        self.vel_y = 5
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
            self.rect.y += self.vel_y
#clase bala
class Bala (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/bala.png')#pygame.Surface([10,30])
        #self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.vel_x = 10
        self.vel_y = 10

    def update(self):
        self.rect.y -= self.vel_y


if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
# grupos
    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    balas_e =pygame.sprite.Group()
#definiendo y agregando elementos a la matriz de sprites
    m = matriz ()
    m2 = matriz2()
# objetos
    jugador = Jugador(m)
    jugador2 = Jugador(m2)
    jugador2.image = jugador2.m[0][0]#pygame.image.load('sprites/nave2.png')#jugador2.m[3][0]

    e = Enemigo()
    e.rect.x = random.randrange(0,ANCHO)
    e.rect.y = random.randrange(-300,0)
    enemigos.add(e)
    todos.add(e)

    jugador2.rect.x = 100
    jugadores.add(jugador2)
    jugadores.add(jugador)
    todos.add(jugador)
    todos.add(jugador2)



    reloj = pygame.time.Clock()
    ptos = 0

    fuente = pygame.font.Font(None, 32)
    fuente2 = pygame.font.Font(None, 32)
    fin = False
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            if event.type == pygame.KEYDOWN:
                print 'keydowm'#jugador.accion = 2
                if event.key == pygame.K_RIGHT:
                    jugador.set_accion(1)
                    jugador.vel_x = 5
                    jugador.vel_y = 0
                if event.key == pygame.K_LEFT:
                    jugador.set_accion(2)
                    jugador.vel_x = -5
                    jugador.vel_y = 0
                if event.key == pygame.K_DOWN:
                    jugador.vel_y = 5
                    jugador.vel_x = 0
                if event.key == pygame.K_UP:
                    jugador.vel_y = -5
                    jugador.vel_x = 0
                if event.key == pygame.K_KP3:
                    b = Bala()
                    b.rect.x = jugador.rect.x+70
                    b.rect.y = jugador.rect.y
                    todos.add(b)
                    balas.add(b)
                    print 'petrosky'
                    jugador.set_accion(0)
                #acciones jugador2
                if event.key == pygame.K_w:
                    jugador2.vel_y = -5
                    jugador2.vel_x = 0
                if event.key == pygame.K_s:
                    jugador2.vel_y += 5
                    jugador2.vel_x = 0
                if event.key == pygame.K_a:
                    jugador2.vel_y = 0
                    jugador2.vel_x = -5
                if event.key == pygame.K_d:
                    jugador2.vel_y = 0
                    jugador2.vel_x = 5
            if event.type == pygame.KEYUP:
                print 'perra'
                if event.key == pygame.K_RIGHT: #or pygame.K_LEFT:
                    jugador.vel_x += -5
                    jugador.accion = 0
                if event.key == pygame.K_d or pygame.K_a:
                    jugador2.vel_x = 0
                    jugador2.accion = 0


                #jugador.vel_y,jugador2.vel_y = 0, 0
                #jugador.vel_x,jugador2.vel_x = 0, 0


        #logica del juego
        #analizar coliciones

        #control de objetos
        for e in enemigos:
            if e.disparar:
                e.temp = random.randrange(100)
                e.disparar=False
                b = Bala()
                b.vel_y = -10
                b.rect.x = e.rect.x
                b.rect.y = e.rect.y
                #b.image.fill(azul)
                balas_e.add(b)
                todos.add(b)

        for b in balas:
            if b.rect.x > ANCHO:
                balas.remove(b)
                todos.remove(b)
        #refresco de pantalla

        todos.update()
        pantalla.fill([0,0,0])
        texto = fuente.render("salud J1", False, [255,255,255])
        salud_valor = fuente.render(str(jugador.salud),False,[255,155,155])
        texto2 = fuente2.render("salud J2", False, [255,255,255])
        salud2_valor = fuente2.render(str(jugador.salud),False,[255,155,155])
        pantalla.blit(texto, [50,10])
        pantalla.blit(texto2, [200,10])
        pantalla.blit(salud_valor, [150, 10])
        pantalla.blit(salud2_valor, [300, 10])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
