import random
import pygame

# Constants
WIDTH, HEIGHT = 1000, 1000
TITLE = "Conway's game of Life"

RESOLUTION = 20
COLS, ROWS = WIDTH // RESOLUTION, HEIGHT // RESOLUTION

# General global variable
running = False
framerate = 30

# Pygame variables
screen = None
clock = None

# My variables
grid = []


def make_grid(rows, cols):
    return [[None for j in range(cols)] for i in range(rows)]


def setup():
    global screen, clock
    global running

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    running = True

    for i in range(ROWS):
        grid.append([])
        for j in range(COLS):
            grid[i].append(random.randint(0,1))


def update_gui():
    screen.fill('black')

    for i in range(ROWS):
        for j in range(COLS):
            x = i * RESOLUTION
            y = j * RESOLUTION
            if grid[i][j] == 1:
                pygame.draw.rect(screen, 'white', pygame.Rect(x, y, RESOLUTION-1, RESOLUTION-1))


    pygame.display.flip()
    clock.tick(framerate)

def update_logic():
    global grid

    new = make_grid(ROWS, COLS)

    for i in range(ROWS):
        for j in range(COLS):
            state = grid[i][j]
            neighbours = 0

            if (i == 0 or i == ROWS - 1) or (j == 0 or j == COLS - 1):
                new[i][j] = state
                continue

            neighbours += grid[i-1][j-1]
            neighbours += grid[i-1][j+1]
            neighbours += grid[i-1][j]
            neighbours += grid[i][j-1]
            neighbours += grid[i][j+1]
            neighbours += grid[i+1][j-1]
            neighbours += grid[i+1][j+1]
            neighbours += grid[i+1][j]

            if state == 0 and neighbours == 3:
                new[i][j] = 1
            elif state == 1 and (neighbours < 2 or neighbours > 3):
                new[i][j] = 0
            else:
                new[i][j] = state
    
    grid = new

def check_inputs():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                running = False

def main():
    setup()
    frame = 0

    while running:
        update_logic()
        update_gui()

        check_inputs()
        frame += 1

        if (frame % framerate) == 0:
            print(clock.get_fps())


if __name__ == "__main__":
    main()