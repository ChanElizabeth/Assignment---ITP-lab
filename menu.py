from pygame import *
import sys
import pygame

def screenMenu(Button, rungame):
    #set the title bar caption and app resolution
    display.set_caption("Meteor Shooter")
    screen = pygame.display.set_mode((800, 600))

    #Create the object button with the image
    btnStart = Button("NewPiskel.png")
    btnQuit = Button("quit button.png")

    #Loads the background and transforms its scale.
    bgImage = pygame.image.load("asteroid_wall.jpg")
    bgImage = pygame.transform.scale(bgImage, (800, 600))

    pygame.init()

    while True:
        #draws the start and quit button at a specific coordinate
        rectStart = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rectQuit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bgImage, (0, 0))
        screen.blit(btnStart.button, (250, 200))
        screen.blit(btnQuit.button, (250, 300))

        #waits for events
        ev = event.wait()

        #if the event is mouse click
        if ev.type == MOUSEBUTTONDOWN:
            if rectStart.collidepoint(mouse.get_pos()):
                rungame()          #run game if the cursor is on the start button
            if rectQuit.collidepoint(mouse.get_pos()):
                sys.exit()      #quit game if the cursor is on the quit button

        if ev.type == QUIT:
            sys.exit()          #quit if user clicks the close button

        display.update()


def pauseMenu(Button, rungame):
    display.set_caption("Meteor Shooter")
    screen = pygame.display.set_mode((800, 600))

    #Create object Button for quit and pause
    startButton = Button("quit button.png")
    returnButton = Button("pause button.png")

    #image for the menu's backgound
    bgImage = pygame.image.load("asteroid_wall.jpg")
    bgImage = pygame.transform.scale(bgImage, (800, 600))

    pygame.init()

    paused = True
    while paused:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bgImage, (0, 0))
        screen.blit(startButton.button, (250, 200))
        screen.blit(returnButton.button, (250, 300))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                screenMenu(Button, rungame)
            if rect_return.collidepoint(mouse.get_pos()):
                paused = False

        if ev.type == QUIT:
            sys.exit()

        display.update()


def gameOverScreen(Button, rungame, score):
    display.set_caption("Meteor Shooter")
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("Times New Roman", 50)
    text = font.render("Game Over. Restart?", True, (255, 255, 255))
    score_text = font.render("score:"+str(score), True, (255, 255, 255))

    startButton = Button("NewPiskel.png")
    quitButton = Button("quit button.png")

    bgImage = pygame.image.load("asteroid_wall.jpg")
    bgImage = pygame.transform.scale(bgImage, (800, 600))

    pygame.init()

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bgImage, (0, 0))
        screen.blit(text, (250, 50))
        screen.blit(startButton.button, (250, 200))
        screen.blit(quitButton.button, (250, 300))
        screen.blit(score_text, (300, 450))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                rungame()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:
            sys.exit()

        display.update()
