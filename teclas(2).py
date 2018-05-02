''' este codigo dibuja un circulo, cuando sobrepasa
la linea de en medio, circula hacia la derecha con v constante
  '''
import pygame
ancho=640; alto=480  #dimensiones
verde = [0,255,0] ; rojo = [255,0,0] ; negro =[0,0,0]
reloj = pygame.time.Clock()  #reloj para manejar tiempo

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    fin = False
    pto = [10,10]
    vel_y=0
    vel_x=0
    rebota = True

    while not fin:

        pto[0]+=vel_x # mueve el punto en x esta en constante cambio
        pto[1]+=vel_y # mueve al punto en y

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    vel_x=0
                    vel_y=-2
                if evento.key == pygame.K_DOWN:
                    vel_x=0
                    vel_y=2
                if evento.key == pygame.K_RIGHT:
                    vel_x=2
                    vel_y=0
                if evento.key == pygame.K_LEFT:
                    vel_x=-2
                    vel_y=0
            if evento.type == pygame.QUIT:
                fin = True
            if evento.type == pygame.KEYUP:
                if pto[0]<ancho/2:
                    vel_x =0
                    vel_y =0
        #-------------------------
        if pto[1]>alto:
            pto[1]=alto-5
            vel_y=0
        #--------------------------
        if pto[1]<0:
            pto[1]=5
            vel_y=0
        #--------------------------
        if pto[0]<0:
            pto[0]=5
            vel_x=0
        #--------------------------
        if pto[0]>ancho/2:
            if(pto[0]<ancho-5  and rebota):
                vel_x = 1
            if(pto[0]==ancho-5):
                vel_x = -1
                rebota = False
        if(not(rebota) and pto[0]<ancho/2):
            rebota= True
            vel_x = 0


        pantalla.fill(negro)
        pygame.draw.line(pantalla,rojo,[ancho/2,0],[ancho/2,alto])
        pygame.draw.circle(pantalla,verde,pto,5)
        pygame.display.flip()
        reloj.tick(100)
