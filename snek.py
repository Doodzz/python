import pygame 
import random
import sys

x=500 #width
y=500 #height
Block_size=20
grid_x=x//Block_size
grid_y=y//Block_size
fps=60

high_score = 0
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass

White=(255,255,255)
Black=(0,0,0)
gray=(50,50,50)
Green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)


screen=pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")

apple_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/apple.png")
apple_image = pygame.transform.scale(apple_image, (Block_size, Block_size))

snake_head_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/snake.png")
snake_body_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/snake_body.png")
snake_body_image = pygame.transform.scale(snake_body_image, (Block_size * 1.5, Block_size * 1.5))




class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (Block_size, 0)
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        new_head = (new_head[0] % x, new_head[1] % y)
        
        self.body.insert(0, new_head)
        
        if self.growing:
            self.growing = False
        else:
            self.body.pop()
    
    def grow(self):
        self.growing = True
    
    def check_collision(self):
        if self.body[0] in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.position = (random.randint(0, (x//Block_size)-1) * Block_size, 
                         random.randint(0, (y//Block_size)-1) * Block_size)
    
    def respawn(self):
        self.position = (random.randint(0, (x//Block_size)-1) * Block_size, 
                         random.randint(0, (y//Block_size)-1) * Block_size)


pygame.init()
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

running = True
while running:
    snake = Snake()
    food = Food()
    score = 0
    speed = 5 
    game_over = False
    
    while not game_over:
        screen.fill(Black)
