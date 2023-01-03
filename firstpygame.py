"""
Started 01/02/2023

Author: phylyp
Remake: camcam95
"""
import os
import pygame

# Centers window on screen/monitor
os.environ["SDL_VIDEO_CENTERED"] = '1'

pygame.init()

# Declarations
boxX, boxY = (120, 120)
windowDimensions = (640, 480)
window = pygame.display.set_mode(windowDimensions)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("First Pygame")
pygame.display.set_icon(pygame.image.load("./assets/firstPygame/icon.png"))

# Colors
BLACK = (0, 0, 0)

while running:
    eventList = pygame.event.get()

    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                boxX += 8
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                boxX -= 8
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                boxY += 8
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                boxY -= 8

    window.fill(BLACK)
    pygame.draw.rect(window, (0, 0, 255), (boxX, boxY, 400, 240))
    pygame.display.update()

clock.tick(60)
pygame.quit()
