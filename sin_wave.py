import pygame
import sys
from math import *

pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Sine Wave')

center = [150,300]
r = 100

theta = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x = center[0] + r * cos(0.01 * theta)
    y = center[1] + r * sin(0.01 * theta)

    screen.fill([50,100,150])

    pygame.draw.circle(screen, 'white', center, r, width=1)
    pygame.draw.circle(screen, 'orange', [round(x),round(y)], 5)
    pygame.draw.circle(screen, 'orange', [400,round(y)], 5)
    theta += 0.01
    
    pygame.display.update()