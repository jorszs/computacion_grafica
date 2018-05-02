import pygame
if __name__ == 'main':
    pygame.init()
    pantalla = pygame.display.set_mode([600,480])
    ptos=[(100,200),(200,100),(150,250),(250,250)]
    pygame.draw.polygon(pantalla,[0,0,255],ptos,1)
    fin = False
    ptos=[]
    pygame.display.flip()
    fin = False
    while not fin:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
                fin=True
