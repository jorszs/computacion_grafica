#
#modificadores : cuando los jugadores elimines a las 3 primeras naves Nave_madre
#                cada que los jugadores eliminen a una nave madre
#

#por hacer
#eliminar enemigos cuando rect.x sea <0 o > ANCHO
#adicionarle las propiedades de modificadores al segundo jugador
#que el jugador pueda exederse un poco a los laterales para que alcance a disparar en los bordes
#recordar : ponerle la aleatoriedad al atributo tipo de la clase modificadores
#ideas : ponerle mas vida a los enemigos. coliciones de enemigos y jugador
#       adicionar naves madre a enemigos para que las balas rastreadoras tambien las identifiquen como objetivos
import pygame
import time
import random
import math
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
        self.bombas = 0
        self.salud = 5
        self.tipo_bala = 0
        self.retardo = 4 #retardo para la aparicion de balas perseguidoras

    def set_accion(self,accion):
        self.accion = accion
    def update(self):
        #actualiza velocidad
        #self.rect.x += self.vel_x
        #controla limites de pantalla
        if self.rect.y >= ALTO/2:
            self.rect.y += self.vel_y

        else:

            self.rect.y = ALTO/2
            self.vel_y = 0
            #posy += -2
        if self.rect.y > (ALTO - self.rect.height):
            self.rect.y = ALTO - self.rect.height


        if self.rect.right <= ANCHO and self.rect.left >= 0:#self.rect.x <= (ANCHO-130) and self.rect.x >= -60:
            self.rect.x += self.vel_x#self.rect.x = ANCHO - 40
        elif self.rect.right >= ANCHO:
            self.rect.right = ANCHO
            self.vel_x = 0

        elif self.rect.left <= 0:
            self.rect.x = 0
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
        self.espera = random.randrange(300)
        self.disparar = False
        self.temp = random.randrange(300)

    def update(self):
        if self.temp > 0:
            self.temp -= 1
        else:
            self.disparar = True
        '''if self.espera > 0:
            self.espera -= 1
        else:'''
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

#clase nave_madre
class Nave_madre(pygame.sprite.Sprite):
    def __init__(self,jugador1,jugador2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,25])
        self.image.fill([55,20,200])
        self.rect = self.image.get_rect()
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.vel_x = 2
        self.vel_y = 3
        self.salud = 10
        self.rect.x = random.randrange(ANCHO)
        self.rect.y = -100
        self.espera = random.randrange(60)
        self.generar = False
        self.temp = random.randrange(60)
        self.tipo = random.randrange(3)
        self.tope = 0
    def update(self):
        if self.temp >0:
            self.temp -= 1
        else:
            self.generar = True
        if self.espera > 0:
            self.espera -=1

        if self.tipo == 0:
            if self.rect.y >= ALTO/6:
                self.rect.y = ALTO/6
                if self.rect.right >= ANCHO:
                    self.vel_x = -2
                elif self.rect.left <= 0:
                    self.vel_x = 2
                self.rect.x += self.vel_x
            else:
                self.rect.y += self.vel_y
        if self.tipo == 1:
            self.rect.x += (self.jugador1.rect.x+ self.jugador1.rect[2]/3 + 7 - self.rect.x)/50
            self.rect.y += (self.jugador1.rect.y+ self.jugador1.rect[3]  - self.rect.y)/50
        if self.tipo == 2:
            self.rect.x += (self.jugador2.rect.x+ self.jugador2.rect[2]/3  - self.rect.x)/50
            self.rect.y += (self.jugador2.rect.y+ self.jugador2.rect[3]  - self.rect.y)/50





#clase bala
class Bala (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,30])#pygame.image.load('sprites/bala.png')#pygame.Surface([10,30])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.enemigos = pygame.sprite.Group()
        self.i = 0#float('inf')
        self.k = {}
        self.tipo = 0
        self.vel_x = 0
        self.vel_y = 10

    def update(self):
        self.rect.y -= self.vel_y
        if self.tipo == 2:

            #for v in self.enemigos:
            #k= {v for v in self.enemigos}
            #print k
            #distancia = [math.sqrt((v.rect.x - self.rect.x)**2 + (v.rect.y - self.rect.y)**2) for v in self.enemigos]
            for v in self.enemigos:
                #self.k[v] = int(math.sqrt((v.rect.x - self.rect.x)**2 + (v.rect.y - self.rect.y)**2))
                self.k[int(math.sqrt((v.rect.x - self.rect.x)**2 + (v.rect.y - self.rect.y)**2))] = v
            if self.k:
                enem = self.k[min(self.k.keys())]
                if enem in self.enemigos:
                    print enem
                    self.rect.x += (enem.rect.x+ enem.rect[2]/2 + 7 - self.rect.x)/7
                    self.rect.y += (enem.rect.y+ enem.rect[3]/2  - self.rect.y)/50
                else:
                    enem = self.k[min(self.k.keys())]

            else:
                pass#self.rect.y -= self.vel_y - 5
            #print self.k
            #self.k[math.sqrt((v.rect.x - self.rect.x)**2 + (v.rect.y - self.rect.y)**2) for v in self.enemigos] = [v for v in self.enemigos]
            '''for v in self.enemigos:
                while self.i <= len(distancia):
                    self.k[v] = distancia[self.i]
                    self.i += 1'''

                #self.k[v]=distancia[i]

        #self.rect.x += self.vel_x

class Bomba(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.image = pygame.Surface([10,30])#pygame.image.load('sprites/bala.png')#pygame.Surface([10,30])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()

        self.tipo = 0
        self.vel_x = 0
        self.vel_y = 10

    def update(self):
        self.rect.y -= self.vel_y

class Modificador (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])#pygame.image.load('sprites/bala.png')#pygame.Surface([10,30])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(20,ANCHO-20)
        self.tipo = 3#random.randrange(4)
        self.vel_x = 0
        self.vel_y = 4

    def update(self):
        self.rect.y += self.vel_y
        #self.rect.x += self.vel_x
if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    '''fondo = Fondo()
    fondo.dibujar()'''
    fondo = pygame.image.load('sprites/fondo_estrella.jpeg')
    info=fondo.get_rect()
    an_fondo = info[2]
    al_fondo = info[3]
    eliminados = 0
    tipo_bala = 0
    posy =  ALTO-al_fondo #variable para controlar el dibujo del fondo
# grupos
    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    naves_madre = pygame.sprite.Group()
    balas_e =pygame.sprite.Group()
    balas_j1 = pygame.sprite.Group()
    balas_j2 = pygame.sprite.Group()
    modificadores = pygame.sprite.Group()
    bombas = pygame.sprite.Group()
#definiendo y agregando elementos a la matriz de sprites
    m = matriz ()
    m2 = matriz2()
# objetos
    jugador = Jugador(m)
    jugador2 = Jugador(m2)
    jugador2.image = jugador2.m[0][0]#pygame.image.load('sprites/nave2.png')#jugador2.m[3][0]
    for e in range(3):
        n = Nave_madre(jugador,jugador2)
        if n.tipo == 1 or n.tipo == 2:
            n.salud = 4
        naves_madre.add(n)
        todos.add(n)
    #e = Enemigo()
    #e.rect.x = random.randrange(0,ANCHO)
    #e.rect.y = random.randrange(-300,0)
    #enemigos.add(e)
    #todos.add(e)

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
                #print 'keydowm'#jugador.accion = 2
                if event.key == pygame.K_RIGHT:
                    jugador.set_accion(1)
                    jugador.vel_y = 0
                    jugador.vel_x = 8

                if event.key == pygame.K_LEFT:
                    jugador.set_accion(2)
                    jugador.vel_y = 0
                    jugador.vel_x = -8

                if event.key == pygame.K_DOWN:
                    jugador.set_accion(0)
                    jugador.vel_y += 8
                    jugador.vel_x =0

                if event.key == pygame.K_UP:
                    jugador.set_accion(0)
                    jugador.vel_y += -8
                    jugador.vel_x = 0

            #condicion para que jugador1 dispare
                if event.key == pygame.K_KP3:
                    b = Bala()
                    b.rect.x = jugador.rect.x+70
                    b.rect.y = jugador.rect.y
                    if jugador.tipo_bala == 2: #tipo_bala = 2 es la bala perseguidora
                        if jugador.retardo == 0:
                            jugador.retardo = 10
                            b.tipo = 0
                            b1 = Bala()
                            b1.tipo = jugador.tipo_bala
                            b2 = Bala()
                            b2.tipo = jugador.tipo_bala
                            b3 = Bala()
                            b3.tipo = jugador.tipo_bala
                            b4 = Bala()
                            b4.tipo = jugador.tipo_bala

                            b1.rect.x = jugador.rect.x + jugador.rect[2]/2 - 60
                            b1.rect.y = jugador.rect.y + jugador.rect[2]/2 - 60
                            b2.rect.x = jugador.rect.x + jugador.rect[2]/2 + 60
                            b2.rect.y = jugador.rect.y + jugador.rect[2]/2 - 60
                            b3.rect.x = jugador.rect.x + jugador.rect[2]/2 - 60
                            b3.rect.y = jugador.rect.y + jugador.rect[2]/2 + 60
                            b4.rect.x = jugador.rect.x + jugador.rect[2]/2 + 60
                            b4.rect.y = jugador.rect.y + jugador.rect[2]/2 + 60


                            l=[[b1,b2,b3,b4]]

                            for v in l[0]:
                                todos.add(v)
                                balas.add(v)
                                balas_j1.add(v)
                                v.enemigos = enemigos

                        else:
                            jugador.retardo -= 1
                            #print jugador.retardo

                    else:
                        b.tipo = jugador.tipo_bala

                    todos.add(b)
                    balas.add(b)
                    balas_j1.add(b)
                    #print 'petrosky'
                    jugador.set_accion(0)


                if event.key == pygame.K_KP0 and jugador.bombas >0:
                    jugador.bombas -= 1
                    bom = Bomba(3)
                    bom.rect.x = jugador.rect.x+70
                    bom.rect.y = jugador.rect.y
                    bombas.add(bom)
                    todos.add(bom)

        #acciones jugador2
                if event.key == pygame.K_w:
                    jugador2.vel_y += -8
                    jugador2.vel_x = 0
                if event.key == pygame.K_s:
                    jugador2.vel_y += 8
                    jugador2.vel_x = 0
                if event.key == pygame.K_a:
                    jugador2.vel_y = 0
                    jugador2.vel_x = -8
                if event.key == pygame.K_d:
                    jugador2.vel_y = 0
                    jugador2.vel_x = 8
            #condicion de disparo jugador2
                if event.key == pygame.K_g:
                    b = Bala()
                    b.rect.x = jugador2.rect.x+20
                    b.rect.y = jugador2.rect.y

                    todos.add(b)
                    balas.add(b)
                    balas_j2.add(b)
        #condiciones de tecla levantada ambos jugadores
            if event.type == pygame.KEYUP:
                #print 'perra'
                if event.key == pygame.K_RIGHT and jugador.vel_x>0: #or pygame.K_LEFT:
                    jugador.vel_x += -5
                    jugador.accion = 0
                if event.key == pygame.K_LEFT and jugador.vel_x<0: #or pygame.K_LEFT:
                    jugador.vel_x += 5
                    jugador.accion = 0
                if event.key == pygame.K_UP and jugador.vel_y<0: #or pygame.K_LEFT:
                    jugador.vel_y += 5
                    jugador.accion = 0
                if event.key == pygame.K_DOWN and jugador.vel_y>0: #or pygame.K_LEFT:
                    jugador.vel_y += -5
                    jugador.accion = 0

                if event.key == pygame.K_d and jugador2.vel_x > 0:
                    jugador2.vel_x += -5
                    jugador2.accion = 0
                if event.key == pygame.K_a and jugador2.vel_x < 0:
                    jugador2.vel_x += 5
                    jugador2.accion = 0

                if event.key == pygame.K_w and jugador2.vel_y<0: #or pygame.K_LEFT:
                    jugador2.vel_y += 5
                    jugador2.accion = 0
                if event.key == pygame.K_s and jugador2.vel_y>0: #or pygame.K_LEFT:
                    jugador2.vel_y += -5
                    jugador2.accion = 0
                #jugador.vel_y,jugador2.vel_y = 0, 0
                #jugador.vel_x,jugador2.vel_x = 0, 0


        #logica del juego
        '''while fondo.rect.y <= ALTO:
            fondo.rect.y += -5
        fondo.rect.y = 0'''
        #control del fondo
        #if posy < 0:
        if jugador.rect.y <= ALTO/2 and jugador2.rect.y <= ALTO/2:
            if posy<0:
                posy += 4
            else:posy = ALTO-al_fondo
        elif posy<0:
            posy +=2
        else:posy = ALTO-al_fondo
            #posy = ALTO-al_fondo


        #analizar coliciones
        for b in balas_e:

            ls_colj = pygame.sprite.spritecollide(b, jugadores, False)
            if jugador in ls_colj:
                balas_e.remove(b)
                todos.remove(b)
                jugador.salud -= 1
                #print 'salud', jugador.salud
            elif jugador2 in ls_colj:
                balas_e.remove(b)
                todos.remove(b)
                jugador2.salud -= 1

        for b in balas:

            if b.tipo == 0 or b.tipo == 2:
                ls_colb = pygame.sprite.spritecollide(b,enemigos,True)
                ls_coln = pygame.sprite.spritecollide(b,naves_madre,False)
                ls_col_be = pygame.sprite.spritecollide(b,balas_e,True)
                for e in ls_colb:
                    e.remove()
                    enemigos.remove(e)
                    todos.remove(e)
                    balas.remove(e)
                    #eliminados +=1
                for e in ls_coln:
                    if e.salud == 0:
                        e.remove()
                        naves_madre.remove(e)
                        todos.remove(e)
                        eliminados += 1
                        #print eliminados
                    balas.remove(b)
                    todos.remove(b)

                    e.salud -= 1
                    #print 'salud nave madre mermando'
            if b.tipo == 1:
                ls_colb = pygame.sprite.spritecollide(b,enemigos,True)
                ls_coln = pygame.sprite.spritecollide(b,naves_madre,False)
                ls_col_be = pygame.sprite.spritecollide(b,balas_e,True)
                #eliminados += 1
                for e in ls_colb:
                    e.remove()
                    enemigos.remove(e)
                    todos.remove(e)
                    balas.remove(e)
                    #eliminados +=1
                for e in ls_coln:
                    if e.salud == 0:
                        e.remove()
                        naves_madre.remove(e)
                        todos.remove(e)
                        eliminados += 1
                        print eliminados
                    balas.remove(b)
                    todos.remove(b)
                    e.salud -= 1

        for j in jugadores:
            ls_coljs = pygame.sprite.spritecollide(j,naves_madre,True)
            ls_colmo = pygame.sprite.spritecollide(j,modificadores,True)

            for e in ls_coljs:
                eliminados += 1
                j.salud -= 1
                e.remove()
                naves_madre.remove(e)
                todos.remove(e)

            for v in ls_colmo:
                if v.tipo == 0:#modificador para aumentar salud
                    j.salud += 2
                if v.tipo == 1:
                    j.tipo_bala = 1 #modificador para generar balarompemuros
                if v.tipo == 2:
                    j.bombas += 1

                if v.tipo == 3:
                    j.tipo_bala = 2

        #control de objetos

        #renovacion de enemivos
        if eliminados == 3:
            eliminados = 0
            for e in range(3):
                n = Nave_madre(jugador,jugador2)
                if n.tipo == 1 or n.tipo == 2:
                    n.espera = random.randrange(60)
                    n.temp = random.randrange(60)
                    n.salud = 4
                naves_madre.add(n)
                todos.add(n)
            for n in range(2):
                n = Modificador()
                modificadores.add(n)
                todos.add(n)
        for e in enemigos:
            if e.disparar:
                e.temp = random.randrange(60)
                e.disparar=False
                b = Bala()
                b.vel_y = -10
                b.vel_x = 0
                b.rect.x = e.rect.x
                b.rect.y = e.rect.y
                #b.image.fill(azul)
                balas_e.add(b)
                todos.add(b)

        for n in naves_madre:
            if n.tipo == 0:
                if n.generar and n.tope < 30 and n.rect.y >= ALTO/6:
                    n.temp = random.randrange(60)
                    n.generar=False
                    n.tope +=1


                    e = Enemigo()
                    e.rect.x = n.rect.x
                    e.rect.y = n.rect.y
                    e.vel_x = random.randrange(-4,4)
                    e.vel_y = 1

                    b = Bala()
                    b.vel_y = -10
                    b.vel_x = 0
                    b.rect.x = n.rect.x
                    b.rect.y = n.rect.y
                    #b.image.fill(azul)
                    balas_e.add(b)
                    todos.add(b)

                    enemigos.add(e)
                    todos.add(e)
        #eliminacion de objetos fuera de calcularPosPantalla
        for b in balas_e:
            if b.rect.y > ALTO:
                b.remove()
                balas_e.remove(b)
                todos.remove(b)

        for b in balas:
            if b.rect.y < 0:
                b.remove()
                balas.remove(b)
                todos.remove(b)
        for e in enemigos:
            if e.rect.y >ALTO:
                e.remove()
                enemigos.remove(e)
                todos.remove(e)
        #refresco de pantalla

        todos.update()
        pantalla.fill([0,0,0])
        texto = fuente.render("salud J1", False, [255,255,255])
        salud_valor = fuente.render(str(jugador.salud),False,[255,155,155])
        texto2 = fuente2.render("salud J2", False, [255,255,255])
        salud2_valor = fuente2.render(str(jugador2.salud),False,[255,155,155])
        pantalla.blit(fondo,[0,posy])
        pantalla.blit(texto, [50,10])
        pantalla.blit(texto2, [200,10])
        pantalla.blit(salud_valor, [150, 10])
        pantalla.blit(salud2_valor, [300, 10])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
