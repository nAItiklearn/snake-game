import pygame , random
import sys
from pygame.math import Vector2
 
class Fruit:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos =Vector2(self.x, self.y)
        
    def draw_fruit(self):
        fruit_rect =pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        pygame.draw.rect(screen, (120, 165, 114) , fruit_rect)
        
       
pygame.init()
cell_size=40
cell_number=20


clock = pygame.Clock()
screen = pygame.display.set_mode((cell_size* cell_number , cell_number*cell_size))
pygame.display.set_caption("SNAKE GAME LOL")
surface = pygame.Surface((100, 200))
surface.fill((0 , 0 , 225))
fruit=Fruit()
rect1= surface.get_rect(center=(250 , 250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((175, 215, 60))
    # screen.blit(surface, rect1)
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
