import random
import pygame

ancho=1000
alto=900
centro=[300,300]
rojo=[255,0,0]
verde=[0,255,0]
negro=[0,0,0]
azul=0x0080FF
morado=0xDF01D7
amarillo=0xFFFF00
blanco=[255,255,255]

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



class Jugador (pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion=1
        self.m=m
        self.image = m[self.accion][0]
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=200
        self.i=0

        self.vel_x = 0
        self.vel_y = 0


    def update(self):
        self.rect.x +=self.vel_x
        self.rect.y +=self.vel_y

        if self.accion == 2:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion =1
        else:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0

        self.image = self.m[self.accion][self.i]

class Barril (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,80])
        #self.image = pygame.image.load('sprite/morty.png')
        self.sonido = pygame.mixer.Sound('explosion1.ogg')
        self.rect=self.image.get_rect()
        self.rect.x=300
        self.rect.y=180
        self.image.fill(blanco)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    limites=[4,4,3,5,2,4,5,5,7,1]
    m=Recortar(10,7,'sprite/ken.png',limites)

    jugadores=pygame.sprite.Group()
    todos=pygame.sprite.Group()
    barriles=pygame.sprite.Group()
    b=Barril()
    todos.add(b)
    barriles.add(b)

    j=Jugador(m)
    jugadores.add(j)
    todos.add(j)
    accion=0
    i=0
    reloj=pygame.time.Clock()

    fin=False
    while not fin:
        #Gestion de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin=True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    j.vel_x = -5
                    j.vel_y = 0
                if evento.key == pygame.K_RIGHT:
                    j.vel_x = 5
                    j.vel_y = 0
                if evento.key == pygame.K_UP:
                    j.vel_x = 0
                    j.vel_y = -5
                if evento.key == pygame.K_DOWN:
                    j.vel_x = 0
                    j.vel_y = 5
                if evento.key == pygame.K_a:
                    j.accion = 2
                    j.i = 0
            if evento.type == pygame.KEYUP:
                j.vel_x = 0
                j.vel_y = 0
        #COLISIONES

        if j.accion == 2:
            ls_col = pygame.sprite.spritecollide(j,barriles,False)
            for e in ls_col:
                if j.rect.bottom <=(e.rect.bottom+20):
                    e.rect.x +=10
                    b.sonido.play()

        #Refresco
        todos.update()
        pantalla.fill(negro)
        todos.draw(pantalla)
        #pantalla.blit(m[accion][i],[ps_x,ps_y])
        pygame.display.flip()
        reloj.tick(20)
