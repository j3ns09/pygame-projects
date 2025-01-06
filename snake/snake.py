import random
import pygame

# Constants
WIDTH, HEIGHT = 600, 600
TITLE = "Snake game"

RESOLUTION = 20
ROWS, COLS = WIDTH // RESOLUTION, HEIGHT // RESOLUTION

# Pygame variables
running = False
screen, clock = None, None

# My variables

# 0 for nothing, 1 for obstacles, 2 for apples
grid = [[0 for j in range(COLS)] for i in range(ROWS)]

# Apple coordinates
apple = (random.randint(0,ROWS-1), random.randint(0,COLS-1))

# Contains coordinates (tuples)
snake = []
snake_set = set()

# Snake direction vector
# 1 being right
# 2 being down
# 3 being left
# 4 being up
vec = 1

def get_apple():
    global apple
    apple = (random.randint(0,ROWS-1), random.randint(0,COLS-1))
    while apple in snake_set:
        apple = (random.randint(0,ROWS-1), random.randint(0,COLS-1))
    


def setup():
    global screen, clock
    global running

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    running = True

    snake.append((ROWS//2, COLS//2))
    snake_set.add(snake[0])

def update_gui():
    screen.fill('black')

    for x, y in snake:
        pygame.draw.rect(screen, 'green', pygame.Rect(x * RESOLUTION, y * RESOLUTION, RESOLUTION - 1, RESOLUTION - 1))
    
    
    ax, ay = apple
    pygame.draw.rect(screen, 'red', pygame.Rect(ax * RESOLUTION, ay * RESOLUTION, RESOLUTION, RESOLUTION))
 

    pygame.display.flip()
    clock.tick(10)

def update_logic():
    global running

    x, y = snake[0]
    if vec == 1:
        x += 1
    elif vec == 2:
        y += 1
    elif vec == 3:
        x -= 1
    elif vec == 4:
        y -= 1

    new_coord = (x,y)

    if new_coord in snake_set:
        print("Game over!")
        running = False

    snake.insert(0, new_coord)
    snake_set.add(new_coord)

    if new_coord == apple:
        get_apple()
    else:
        tail = snake.pop()
        snake_set.remove(tail)

def check_inputs():
    global vec
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                running = False
            
            if event.key == pygame.K_RIGHT and vec != 3:
                vec = 1
            if event.key == pygame.K_DOWN and vec != 4:
                vec = 2
            if event.key == pygame.K_LEFT and vec != 1:
                vec = 3
            if event.key == pygame.K_UP and vec != 2:
                vec = 4

def main():
    setup()

    while running:
        update_logic()
        update_gui()

        check_inputs()

if __name__ == '__main__':
    main()