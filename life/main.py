import random
import pygame
import numpy as np
# if numba is installed
import numba

# Constants
WIDTH : int = 1000
HEIGHT : int = 1000
TITLE : str = "Conway's game of Life"

RESOLUTION : int = 10

COLS : int = WIDTH // RESOLUTION
ROWS : int = HEIGHT // RESOLUTION

coord_mask : int = 0xFFFF

# General global variable
running : bool = False
framerate : int = 30

# Pygame variables
screen : None | pygame.Surface = None
clock : None | pygame.time.Clock = None

# My variables
grid : np.ndarray | None = None

@numba.njit(parallel=True)
def get_random_grid(rows, cols) -> np.ndarray:
    new = np.zeros((rows * cols))
    for i in numba.prange(rows):
        for j in numba.prange(cols):
            new[i * cols + j] = random.randint(0,1)
    return new


def setup() -> None:
    global screen, clock
    global running
    global grid

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)

    running = True
    grid = get_random_grid(ROWS, COLS)

# @numba.njit(parallel=True)
def get_rects(grid) -> np.ndarray:
    temp_grid : np.ndarray = [pygame.Rect(j, i, RESOLUTION - 1, RESOLUTION - 1) for i in range(ROWS) for j in range(COLS) if grid[i * COLS + j] == 1]
    # for i in range(ROWS):
    #     for j in range(COLS):
    #         if grid[i * COLS + j] == 1:
    #             rect = pygame.Rect(j, i, RESOLUTION - 1, RESOLUTION - 1)
    #             temp_grid[i * COLS + j] = rect
    return temp_grid


def update_gui() -> None:
    screen.fill('black')

    rects = get_rects(grid)

    for rect in rects:
        screen.fill("white", rect)

    pygame.display.flip()
    clock.tick(framerate)

# use if numba is installed
# @numba.njit(parallel=True)
def get_states(grid) -> np.ndarray:
    new = np.zeros((ROWS * COLS))

    for i in numba.prange(1, ROWS - 1):
        for j in numba.prange(1, COLS - 1):
            index = i * COLS + j
            state : int = grid[index]
            neighbours : int = 0

            # left
            neighbours += grid[index - 1]
            
            neighbours += grid[index - 1 - COLS]
            neighbours += grid[index - 1 + COLS]
            
            # up
            neighbours += grid[index - COLS]

            # down
            neighbours += grid[index + COLS]
            
            neighbours += grid[index + 1 - COLS]
            neighbours += grid[index + 1 + COLS]
            
            # right
            neighbours += grid[index + 1]

            if state == 0 and neighbours == 3:
                new[index] = 1
            elif state == 1 and (neighbours < 2 or neighbours > 3):
                new[index] = 0
            else:
                new[index] = state
    return new

def update_logic() -> None:
    global grid

    grid = get_states(grid)

def check_inputs() -> None:
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                running = False

def main() -> None:
    setup()
    frame : int = 0

    while running:
        update_logic()
        update_gui()

        check_inputs()
        frame += 1

        if (frame % framerate) == 0:
            print(clock.get_fps())


if __name__ == "__main__":
    main()