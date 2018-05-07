import pygame
import random

Alto=480
Ancho=640
Rojo=[255,0,0]
Verde=[0,255,0]
Blanco=[255,255,255]
Negro=[0,0,0]
Azul=[0,0,100]



class Jugador(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.i = 0
        #self.m = m
        #self.gravedad()
        self.vel_x = 0
        self.vel_y = 0
        self.accion = 0
        self.image = pygame.Surface([an,al])#m[self.accion][0]#self.image.fill(verde)
        self.image.fill(Verde)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.pls=None#platafomas

    def gravedad(self, val):
        if self.vel_y >= 0:
            self.vel_y += 1
        else:
            self.vel_y += val
    def update(self):
        self.gravedad(0.8)
        self.rect.y += self.vel_y


        if self.rect.y <= (Alto - self.rect.height):
            self.rect.y = Alto - self.rect.height
            #  self.vel_y = 0

        col = pygame.sprite.spritecollide(self, self.pls,False)
        for p in col:
            if (sel.vel_y<=0) and self.rect.top <= p.rect.bottom:
                self.rect.top = p.rect.bottom
                self.vel_y+=1.5
            elif (sel.vel_y>0) and self.rect.bottom >= (p.rect.top-self.rect.height):
                self.rect.bottom = (p.rect.top-self.rect.height)
                self.vel_y = 0
                self.gravedad(0)
        col = pygame.sprite.spritecollide(self, self.pls, False)
        for p in col:
            if (sel.vel_x>0) and self.rect.right >= p.rect.left:
                self.rect.right = p.rect.left
            elif (sel.vel_x<0) and self.rect.left >= p.rect.right:
                self.rect.left = p.rect.right


        self.rect.x += self.vel_x

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, al])
        self.image.fill(Blanco)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.dir = 0
    def update(self):
        if self.rect.x <= 400:
            self.vel_x += 2
        else:
            self.vel_x += -2


if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    #imagen = pygame.image.load('sprite/animals1.png')


    todos = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    pl = Plataforma(100,30)
    pl.rect.y = 300
    pl.rect.x = 350
    plataformas.add(pl)
    todos.add(pl)
    j = Jugador(40,60)
    j.rect.x = 20
    j.rect.x = 30
    j.pl=plataformas
    todos.add(j)
    reloj=pygame.time.Clock()
    fin=False

    i=0
    px = 0
    vel_x =1
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.vel_x = 5
                if event.key == pygame.K_LEFT:
                    j.vel_x = -5
                if event.key == pygame.K_UP:
                    j.vel_y += -10
            if event.type == pygame.KEYUP:
                j.vel_x = 0

        for p in plataformas:
            if p.rect.x==400 :
                p.dir=1
            elif p.rect.x ==100:
                p.dir = 0
        todos.update()
        todos.draw(pantalla)
        pantalla.fill([0,0,0])

        pygame.display.flip()
        reloj.tick(50)
