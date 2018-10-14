from pygame import *
from pygame.sprite import *


class button(Sprite):
    #initialize the button
    def __init__(self, image):
        #inherit from Sprite
        Sprite. __init__(self)

        #loads the image of the button on the screen and transform its scale
        self.button = pygame.image.load(image)
        self.button = pygame.transform.scale(self.button, (300, 150))
