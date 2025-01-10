import random
import pygame

# Constants
WIDTH, HEIGHT = 600, 600
TITLE = "Snake game"

RESOLUTION = 6
ROWS, COLS = WIDTH // RESOLUTION, HEIGHT // RESOLUTION

# Pygame variables
running = False
screen, clock = None, None

# My variables

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

boosting = False

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
        pygame.draw.rect(screen, 'green', pygame.Rect(x * RESOLUTION, y * RESOLUTION, RESOLUTION, RESOLUTION))
        # pygame.draw.circle(screen, 'green', (x * RESOLUTION, y * RESOLUTION), RESOLUTION//3)
    
    ax, ay = apple
    pygame.draw.rect(screen, 'red', pygame.Rect(ax * RESOLUTION, ay * RESOLUTION, RESOLUTION, RESOLUTION))
    # pygame.draw.circle(screen, 'red', (ax * RESOLUTION, ay * RESOLUTION), RESOLUTION//3)

    pygame.display.flip()
    if not boosting:
        clock.tick(10)
    else:
        clock.tick(60)

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

    if new_coord in snake_set or (new_coord[0] > COLS or new_coord[0] < 0) or (new_coord[1] > ROWS or new_coord[1] < 0):
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
    global boosting

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
            
            if event.key == pygame.K_SPACE:
                boosting = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                boosting = False
def main():
    setup()

    while running:
        check_inputs()
        
        update_logic()
        update_gui()


if __name__ == '__main__':
    main()
