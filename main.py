import pygame , random
import sys
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body=[Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
        
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            
            block_rect= pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,(50,100, 50),block_rect)
    
    def move(self):
        body_copy = self.body[:-1] #copy the whole body except face
        body_copy.insert(0, self.body[0]+ self.direction)
        
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
snake =Snake()
rect1= surface.get_rect(center=(250 , 250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((175, 215, 60))
    # screen.blit(surface, rect1)
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
