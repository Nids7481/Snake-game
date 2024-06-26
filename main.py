#pygame window
import pygame 
from pygame.locals import *
import time
import random

SIZE=40

class Apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x=SIZE*3
        self.y=SIZE*3
    
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x=random.randint(1,24)*SIZE 
        self.y=random.randint(1,19)*SIZE

class Snake:
    def __init__(self,parent_screen,length):
        self.parent_screen=parent_screen
        self.block = pygame.image.load("resources/block1.jpg").convert()
        self.length=length
        self.x=[40]*length #empty array of size length
        self.y=[40]*length
        self.direction= 'down'

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((0,200,0))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i])) #draw block
        pygame.display.flip()

    def move_left(self):
        self.direction='left'

    def move_right(self):
        self.direction='right'

    def move_up(self):
        self.direction='up'
    
    def move_down(self):
        self.direction='down'
    
    def walk(self):
        for i in range(self.length -1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()


class Game:
    def __init__(self):
         pygame.init()
         pygame.display.set_caption("Snake")
         pygame.mixer.init()

         self.surface = pygame.display.set_mode((1000,800)) #inititalize game window
         self.surface.fill((0,200,0))
         self.snake=Snake(self.surface,1)
         self.snake.draw()
         self.apple=Apple(self.surface)
         self.apple.draw()


    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1< x2 +SIZE:
            if y1 >= y2 and y1< y2  +SIZE:
                return True
        return False
    
    
    
    def play(self):
        self.snake.walk() #walks w/o pressing a key
        self.apple.draw() 
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()
        
        for i in range(1,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):

               raise "Game over"


    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score=font.render(f"Score:{self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(800,10))
    
    def show_game_over(self):
        self.surface.fill((0,200,0))
        font = pygame.font.SysFont('arial',30)
        Line1=font.render(f"Game is over! Your score is {self.snake.length}",True,(255,255,255))    
        self.surface.blit(Line1,(200,300))
        Line2=font.render("To play again press Enter. To exit press Escape",True,(255,255,255))
        self.surface.blit(Line2,(200,350))
        pygame.display.flip()
    
    def reset(self):
        self.snake=Snake(self.surface,1)
        self.apple=Apple(self.surface)


    def run(self):
        running = True
        pause=False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key== K_ESCAPE:   #closes window with esc
                        running=False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key== K_UP: #y cord changes 
                            self.snake.move_up()
                        if event.key== K_DOWN: #y cord changes 
                            self.snake.move_down()
                        if event.key== K_LEFT: #x cord changes 
                             self.snake.move_left()       
                        if event.key== K_RIGHT: #x cord changes 
                            self.snake.move_right()

                elif event.type == QUIT:
                    running=False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause=True
                self.reset()
            
            time.sleep(0.3)

        
if __name__ == "__main__":
    game = Game()
    game.run()

   

    
    
    


    


