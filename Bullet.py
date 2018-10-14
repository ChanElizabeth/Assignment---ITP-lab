from pygame import *
from pygame.sprite import *

class Bullet(Sprite):
    def __init__(self, screen, startX, startY):
        Sprite. __init__(self)

        self.startX = startX
        self.startY = startY
        self.speedX = 20

        #loads the image and transforms its scale.
        self.image = image.load("bullets.png")
        self.image = transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        self.rect.left = startX
        self.rect.top = startY
        self.rect.center = (startX, startY)
        self.screen = screen

    #move the bullet to the right
    def movement(self):
        self.rect.left += self.speedX
