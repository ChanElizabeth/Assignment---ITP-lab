from pygame import *

class starBg:
    #initializes baxkground setting
    def __init__(self, ai_settings, background):
        self.background = image.load(background)
        self.background = transform.scale(self.background, (ai_settings.screen_width,
                                           ai_settings.screen_height))
        self.backgroundSize = self.background.get_size()
        self.backgroundRect = self.background.get_rect()
        self.width, self.height = self.backgroundSize

    #draws the background
    def draw(self, screen, x, y):
        screen.blit(self.background, (x, y))

