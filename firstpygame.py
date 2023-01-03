"""
Started 01/02/2023

Author: phylyp
Remake: captainhawaii

GameLoop
    +init()
    +processInput()
    +update()
    +render()
    +run()
"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    pygame.display.update()

pygame.quit()