import pygame , random
import sys
from pygame.math import Vector2


def load_sound(path):
    try:
        return pygame.mixer.Sound(path)
    except (pygame.error, FileNotFoundError) as error:
        print(f"sound unavailable:{path}({error})")
        return None
class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('snake/head_up.png').convert_alpha()
        self.head_down = pygame. image.load('snake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('snake/head_right.png').convert_alpha()
        self.head_left = pygame. image. load('snake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('snake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('snake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('snake/tail_right.png').convert_alpha()
        self.tail_left = pygame. image. load('snake/tail_left.png').convert_alpha()

        self.body_vertical = pygame. image. load('snake/body_vertical.png') .convert_alpha()
        self.body_horizontal = pygame.image.load('snake/body_horizontal.png').convert_alpha()

        self.body_tr= pygame. image. load('snake/body_tr.png'). convert_alpha()
        self.body_tl = pygame.image.load('snake/body_tl.png').convert_alpha()
        self.body_br= pygame.image.load('snake/body_br.png'). convert_alpha()
        self.body_bl = pygame.image.load('snake/body_bl.png').convert_alpha()
        
    def draw_snake(self):
        for index, block in enumerate(self.body):
            #for positioning
            x_pos = int(block.x* cell_size)
            y_pos =int(block.y *cell_size)
            blockRect =pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            #2. what direction is the face heading 
            if index==0:
                if self.direction == Vector2(1,0):
                    block_image = self.head_right
                elif self.direction==Vector2(-1,0):
                    block_image =self.head_left
                elif self.direction ==Vector2(0,-1):
                    block_image= self.head_up
                elif self.direction ==Vector2(0,1):
                    block_image=self.head_down
            elif index == len(self.body)-1:
                tailR = self.body[-2] -self.body[-1]
                if tailR == Vector2(1,0):
                    block_image = self.tail_left
                elif tailR == Vector2(-1,0):
                    block_image = self.tail_right
                elif tailR ==Vector2(0,1):
                    block_image =self.tail_up
                else:
                    block_image = self.tail_down
                    
           
            else:
                head_side = self.body[index - 1] - block
                tail_side = self.body[index + 1] - block

                # Straight body segments
                if head_side.x == tail_side.x:
                    block_image = self.body_vertical

                elif head_side.y == tail_side.y:
                    block_image = self.body_horizontal

                # Corner body segments
                else:
                    if head_side.x == 1 or tail_side.x == 1:
                        if head_side.y == -1 or tail_side.y == -1:
                            block_image = self.body_tr
                        else:
                            block_image = self.body_br
                    else:
                        if head_side.y == -1 or tail_side.y == -1:
                            block_image = self.body_tl
                        else:
                            block_image = self.body_bl

            screen.blit(block_image, blockRect)

                
                             
    def move(self):
        if self.new_block== True:
            body_copy = self.body[:]
            body_copy.insert(0, self.body[0]+ self.direction)
            self.body =body_copy[:]
            self.new_block=False    
        else:
            body_copy = self.body[:-1] #copy the whole body except face
            body_copy.insert(0, self.body[0]+ self.direction)
            self.body =body_copy[:]
    
    
        
    def add_block(self):
        self.new_block= True
        
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
        self.score =0
        self.game_over =False    
        self.score_font=pygame.font.Font(None, 36)
        self.message_font =pygame.font.Font(None, 32)
        self.title_font =pygame.font.Font(None , 80)
        
        self.eat=load_sound("sound.mp3")
    
    def reset(self):
        self.snake =Snake()
        self.villain=villain()
        while self.villain.pos in self.snake.body:
            self.villain.randomzie()
        
        self.score=0
        self.game_over=False 
        
        
    def update(self):
        if self.game_over:
            return
        self.snake.move()
        self.collision()
        self.check_fail()
    
    def draw(self):
        self.villain.draw_villain()
        self.snake.draw_snake()
        score_text = self.score_font.render(f"SCORE:{self.score}",True,(225, 155,65))
        screen.blit(score_text,(15,15))
        if self.game_over:
            overlay =pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            overlay.fill((5, 2, 15, 221))
            screen.blit(overlay,(0,0))
            title =self.title_font.render("DIEDD", True, (225, 0, 0))
            final_score =self.message_font.render(f"TOTAL SCORE: {self.score}",True,(225, 210,0))
            gameText =self.message_font.render("you are caught by the pumpkin king 67..", True, (200, 180, 0))
            replayText = self.message_font.render("PRESS R TO REPLAY , esc TO QUET", True, (225, 155,65))
            center_x =screen.get_width() //2
            center_y = screen.get_height()//2
            screen.blit(title, title.get_rect(center =(center_x,center_y-60)))
            screen.blit(final_score, final_score.get_rect(center=(center_x, center_y)))
            screen.blit(gameText, gameText.get_rect(center=(center_x,center_y+60)))
            screen.blit(replayText, replayText.get_rect(center= (center_x, center_y+100)))
        
        
        
    def collision(self):
        if self.villain.pos== self.snake.body[0]:
            self.score+=1
            if self.eat:
                self.eat.play()
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
            if block == head:
                self.gameover()
                
    def gameover(self):
        self.game_over=True
    
        
      
       
pygame.init()
cell_size=40
cell_number=20
screen = pygame.display.set_mode((cell_size* cell_number , cell_number*cell_size))
pygame.display.set_caption("SNAKE GAME LOL")
backgroud = pygame.image.load("background.png").convert()
backgroud = pygame.transform.scale(backgroud, (cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()
surface = pygame.Surface((100, 200))
mainGame = main()
villain_img = pygame.image.load('image.png').convert_alpha()
villain_img =pygame.transform.scale(villain_img,(40,40))

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
            if mainGame.game_over:
                if event.key ==pygame.K_r:
                    mainGame.reset()
                elif event.key ==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            else:
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
     
    screen.blit(backgroud,(0,0))
    mainGame.draw()
    pygame.display.update()
    clock.tick(60)
