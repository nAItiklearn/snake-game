import pygame , random
import sys
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body=[Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.newBlock=False
        self.direction = Vector2(1,0)
        
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            
            block_rect= pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,(50,100, 50),block_rect)
    
    def move(self):
        if self.newBlock== True:
            body_copy = self.body[:]
            body_copy.insert(0, self.body[0]+ self.direction)
            self.body =body_copy[:]
            self.newBlock=False
        else:
            body_copy = self.body[:-1] #copy the whole body except face
            body_copy.insert(0, self.body[0]+ self.direction)
            self.body =body_copy[:]
    
    
        
    def add_block(self):
        self.newBlock= True
        
class villain:
    def __init__(self):
        self.randomzie()
    def randomzie(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos =Vector2(self.x, self.y)
        
    def draw_villain(self):
        villain_rect =pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(villain_img, villain_rect)
      
class main:
    def __init__(self):
        self.snake = Snake()
        self.villain=villain()
        
    def update(self):
        self.snake.move()
        self.collision()
        self.check_fail()
    
    def draw(self):
        self.villain.draw_villain()
        self.snake.draw_snake()
        
    def collision(self):
        if self.villain.pos== self.snake.body[0]:
            self.villain.randomzie()
            self.snake.add_block()
    def check_fail(self):
        head= self.snake.body[0]
        #for checking if its touch wall or itself
        if head.x<0 or head.x>=cell_number:
            self.gameover()
        if head.y<0 or head.y>= cell_number:
            self.gameover()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()
                
    def gameover(self):
        pygame.quit()
        sys.exit()
    
        
      
       
pygame.init()
cell_size=40
cell_number=20


clock = pygame.time.Clock()
screen = pygame.display.set_mode((cell_size* cell_number , cell_number*cell_size))
pygame.display.set_caption("SNAKE GAME LOL")
surface = pygame.Surface((100, 200))
surface.fill((0 , 0 , 225))

mainGame = main()
villain_img = pygame.image.load('villain.png').convert_alpha()

SCREENUPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREENUPDATE, 150)
rect1= surface.get_rect(center=(250 , 250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type ==SCREENUPDATE:
            mainGame.update()
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                if mainGame.snake.direction.y!=1:
                 mainGame.snake.direction=Vector2(0,-1)
            if event.key ==pygame.K_DOWN:
                 if mainGame.snake.direction.y!=-1:
                  mainGame.snake.direction =Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if mainGame.snake.direction.x!=1:
                 mainGame.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if mainGame.snake.direction.x!=-1:
                 mainGame.snake.direction = Vector2(1,0)
     
    screen.fill((175, 215, 60))
    mainGame.draw()
    pygame.display.update()
    clock.tick(60)
