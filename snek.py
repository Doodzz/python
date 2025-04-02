import pygame 
import random
import sys

x=500 #width
y=500 #height
Block_size=20
grid_x=x//Block_size
grid_y=y//Block_size
fps=60

White=(255,255,255)
Black=(0,0,0)
gray=(50,50,50)

screen=pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")

apple_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/apple.png")
#apple_image = pygame.transform.scale(apple_image)

snake_head_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/snake.png")
snake_body_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/snake_body.png")
#snake_body_image = pygame.transform.scale(snake_body_image)


class Snake:
    print() #temp

class Food:
    print() #temp


class powerups:
    print() # temp
    

running=True
while running:
    snake = Snake()
    food = Food()
    score = 0
    speed = 5  
    game_over = False
    
    while not game_over:
        screen.fill(Black)