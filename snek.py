import pygame 
import random
import sys

x=500 #Width
y=500 #Height
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
Grey=(50,50,50)
Green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)


screen=pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")

apple_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/apple.png")
apple_image = pygame.transform.scale(apple_image, (Block_size, Block_size))

snake_head_image = pygame.image.load("C:/piss code/.vs/shitstain/testing.py/Assets/snake.png")
snake_head_image_original = pygame.transform.scale(snake_head_image, (Block_size, Block_size))
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


class PowerUp:
    Types = ["2x", "slow", "fast"]
    Color = {"2x": red, "slow": blue, "fast": Green}

    def __init__(self):
        self.type = random.choice(self.Types)
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, (x//Block_size)-1) * Block_size,
                random.randint(0, (y//Block_size)-1) * Block_size)

    def respawn(self):
        self.type = random.choice(self.Types)
        self.position = self.random_position()


pygame.init()
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

running = True
while running:
    snake = Snake()
    food = Food()
    powerup = PowerUp()
    powerup_end_time = 0
    score = 0
    speed = 5  
    Multiplier = 1
    game_over = False
    
    while not game_over:
        screen.fill(Black)

        #Rutnät
        for line_x in range(0, x, Block_size):
            pygame.draw.line(screen, Grey, (line_x, 0), (line_x, y))
        for line_y in range(0, y, Block_size):
            pygame.draw.line(screen, Grey, (0, line_y), (x, line_y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, Block_size):
                    snake.direction = (0, -Block_size)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -Block_size):
                    snake.direction = (0, Block_size)
                elif event.key == pygame.K_LEFT and snake.direction != (Block_size, 0):
                    snake.direction = (-Block_size, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-Block_size, 0):
                    snake.direction = (Block_size, 0)
        snake.move()
        
        if snake.body[0] == food.position:
            snake.grow()
            food.respawn()
            score += 1 * Multiplier
            speed = min(15, speed + 1)  
        
        if snake.body[0] == powerup.position:
            if powerup.type == "2x":
                Multiplier = 2
                powerup_end_time = pygame.time.get_ticks() + 5000
            elif powerup.type == "slow":
                speed = max(2, speed - 2)
            elif powerup.type == "fast":
                speed = min(20, speed + 3)
            powerup.respawn()

        if pygame.time.get_ticks() > powerup_end_time:
            Multiplier = 1

        if snake.check_collision():
            game_over = True
        
        screen.blit(apple_image, food.position)
        pygame.draw.rect(screen, PowerUp.Color[powerup.type], pygame.Rect(powerup.position, (Block_size, Block_size)))
        
        for index, segment in enumerate(snake.body):
            if index == 0:
                if snake.direction == (Block_size, 0):
                    rotated_head = snake_head_image_original
                elif snake.direction == (-Block_size, 0):
                    rotated_head = pygame.transform.rotate(snake_head_image_original, 180)
                elif snake.direction == (0, -Block_size):
                    rotated_head = pygame.transform.rotate(snake_head_image_original, 90)
                elif snake.direction == (0, Block_size):
                    rotated_head = pygame.transform.rotate(snake_head_image_original, -90)
                screen.blit(rotated_head, segment)
            else:
                screen.blit(snake_body_image, segment)
        
        score_text = font.render(f"Score: {score}", True, White)
        high_score_text = font.render(f"High Score: {high_score}", True, White)
        screen.blit(score_text, (x - 120, 10))
        screen.blit(high_score_text, (x - 160, 30))
        
        pygame.display.flip()
        clock.tick(speed)
    
    if score > high_score:
        high_score = score
        with open("highscore.txt", "w") as file:
            file.write(str(score))
    
    screen.fill(Black)
    game_over_text = font.render("Game Over! Play again? (Y/N)", True, White)
    screen.blit(game_over_text, (x//2 - 120, y//2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting = False
                elif event.key == pygame.K_n:
                    running = False
                    waiting = False

pygame.quit()