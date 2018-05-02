from pygame.locals import *
import pygame

class Player:
    x = 10
    y = 10
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed
    def moveLeft(self):
        self.x = self.x - self.speed
    def moveUp(self):
        self.y = self.y - self.speed
    def moveDown(self):
        self.y = self.y + self.speed

class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self.run = True
        self.pantalla = None
        self.image = None
        self.player = Player()
    def on_init(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption(' MI VENTANA malentina')
        self.run = True
        self.image = pygame.image.load("pygame.png").convert()
    def on_event(self, event):
        if event.type == QUIT:
            self.run = False
    def on_loop(self):
        pass
    def on_render(self):
        self.pantalla.fill((0,0,0))
        self.pantalla.blit(self.image,(self.player.x,self.player.y))
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self.run = False

        while( self.run ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            print ('1 if')
            if (keys[K_RIGHT]):
                self.player.moveRight()

            print ('2 if')
            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self.run = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
