from pygame import *
from pygame.sprite import *

class Jet(Sprite):
    #initialize the Jet
    def __init__(self, screen):
        Sprite.__init__(self)

        #loads the image and transforms its scale
        self.image = image.load("battlejet.png")
        self.image = pygame.transform.scale(self.image, (90, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 50
        self.screen = screen
        self.move_Speed = 6
        self.bulletRate = 2

    #move the jet to the left by decreasing x coordinates
    def moveLeft(self):
        self.rect.x -= self.move_Speed
        display.flip()

    #move the jet to the right by increasing x coordinates
    def moveRight(self):
        self.rect.x += self.move_Speed
        display.flip()

    #move the jet up by decreasing y coordinates
    def moveUp(self):
        self.rect.y -= self.move_Speed
        display.flip()

    #move the jet down by increasing y coordinates
    def moveDown(self):
        self.rect.y += self.move_Speed
        display.flip()
