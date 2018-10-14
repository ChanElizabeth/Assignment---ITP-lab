from pygame import *
from pygame.sprite import *

class Asteroid(Sprite):
    #initialize the asteroid
    def __init__(self, screen, width, height, speedX, startX, startY):
        #inherit sprite
        Sprite.__init__(self)

        #initialize the starting point and speed
        self.startX = startX
        self.startY = startY
        self.speedX = speedX

        #loads the image and transforms its scale.
        self.image = image.load("meteor.png")
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left = startX
        self.rect.top = startY
        self.screen = screen

    #Move the asteroid to the left by decreasing the X coordinate
    def movement(self):
        self.rect.left -= self.speedX
