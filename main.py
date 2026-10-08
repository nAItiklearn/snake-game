import pygame 
import sys
 
pygame.init()
WINDOW_WIDTH = 1120
WINDOW_HEIGHT =720

clock = pygame.Clock()


screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
pygame.display.set_caption("SNAKE GAME LOL")
surface = pygame.Surface((100, 200))
surface.fill((0 , 0 , 225))

rect1= surface.get_rect(center=(250 , 250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((175, 215, 60))
    screen.blit(surface, rect1)
    pygame.display.update()
    clock.tick(60)
