import pygame 
import sys
 
pygame.init()
WINDOW_WIDTH = 1120
WINDOW_HEIGHT =720


screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()

