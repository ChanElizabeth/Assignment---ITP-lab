from pygame import *
import menu
import random

from Jet import *
from Asteroid import *
from Bullet import *
from Button import *
from Starbg import *

def rungame():
    #initialize variables and display of the pygame
    screen = pygame.display.set_mode((800, 600))
    display.set_caption("Meteor Shooter")

    scores = 0
    gameClock = pygame.time.Clock()
    bg_Image = starBg("star.gif")

    #initialize the coordinate of the background
    x = 0
    y = 0
    x1 = bg_Image.width
    y1 = 0

    pygame.init()

    #create object jet, asteroid sprite group, and bullets sprite group
    jet = Jet(screen)
    jetSprites = sprite.Group(jet)
    asteroid_group = sprite.Group()
    bullets = sprite.Group()

    tickRate = 40
    asteroid_timer = pygame.time.get_ticks()
    while True:
        #game phase goes faster after every frame
        gameClock.tick(tickRate)
        tickRate += 0.01

        #change the coordinate of the bg_Image, and draws the background
        x -= 5
        x1 -= 5
        bg_Image.draw(screen, x, y)
        bg_Image.draw(screen, x1, y1)
        if x < -bg_Image.width:
            x = 0
        if x1 < 0:
            x1 = bg_Image.width

        #show score on the screen
        font = pygame.font.SysFont("Times New Roman", 36)
        score = font.render("score:"+str(scores), True, (255, 255, 255))
        screen.blit(score, (10, 550))

        #draw the sprites
        jetSprites.draw(screen)
        bullets.draw(screen)
        asteroid_group.draw(screen)
        display.update()  # update jet and screen view

        #gets user events, and do the movement depending on the event
        event.get()
        key = pygame.key.get_pressed()
        if key[K_LEFT] and jet.rect.x > 0:
            jet.moveLeft()

        if key[K_RIGHT] and jet.rect.x <= 700:
            jet.moveRight()

        if key[K_DOWN] and jet.rect.y <= 500:
            jet.moveDown()

        if key[K_UP] and jet.rect.y > 0:
            jet.moveUp()

        if key[K_SPACE] and len(bullets) <= jet.bulletRate+(scores/4000):
            bullet = Bullet(screen, jet.rect.x+50, jet.rect.y+42)
            bullets.add(bullet)
            pygame.mixer.music.load("LaserBlast.wav")
            pygame.mixer.music.play()

        if key[K_ESCAPE]:
            menu.screenMenu(button, rungame)

        if key[K_p]:
            menu.pauseMenu(button, rungame)

        #release asteroids on the screen in random location speed and starting points
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1, 4)
                                * 6, 800, (random.randint(1, 28) * 20))
            asteroid_group.add(asteroid)
            asteroid_timer = pygame.time.get_ticks()

        #movement of the asteroid
        for asteroid in asteroid_group:
            asteroid.movement()
            #remove the asteroid if it has left the screen
            if asteroid.rect.right <= 0:
                asteroid_group.remove(asteroid)
            #check if the jet collides with the asteroid
            if sprite.groupcollide(jetSprites, asteroid_group, dokilla=True, dokillb=True):
                menu.gameOverScreen(button, rungame, scores)

        #movement of the bullets
        for bullet in bullets:
            bullet.movement()
            #remove the bullet if it has left the screen
            if bullet.rect.left > 800:
                bullets.remove(bullet)
            #check if the bullet collides with the asteroid
            if sprite.groupcollide(bullets, asteroid_group, dokilla=True, dokillb=True):
                scores += 100


#run the game by calling the main menu
menu.screenMenu(button, rungame)
